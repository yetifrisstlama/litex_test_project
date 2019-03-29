`timescale 1 ns / 1 ps

module IserdesSp6_tb;
    localparam real SYS_CLK_PERIOD = 1e9 / 100e6;    // Simulated clock period in [ns]
    localparam real FR_CLK_PERIOD = 1e9 / 125e6 * 2; // DDR
    localparam real DCO_CLK_PERIOD = FR_CLK_PERIOD / 8.0; // DDR

    //------------------------------------------------------------------------
    // Clock and fake LVDS lanes generation
    //------------------------------------------------------------------------
    reg sys_clk = 1;
    reg fr_clk = 1;
    reg dco_clk_p = 0;
    reg out_a_p = 0;
    reg out_b_p = 0;
    always #(SYS_CLK_PERIOD / 2) sys_clk = ~sys_clk;
    always #(FR_CLK_PERIOD / 2) fr_clk = ~fr_clk;
    initial begin
        #(DCO_CLK_PERIOD / 4.2);
        forever #(DCO_CLK_PERIOD / 2) dco_clk_p = ~dco_clk_p;
    end
    // reg [15:0] testPattern = 16'b1110000000000010;
    reg [15:0] testPattern = 16'b0000000000001101;
    reg [15:0] temp = 0;
    always begin
        // Craft 2 x 8 bit DDR signals according to timing diagram in LTC datasheet
        temp = testPattern;
        repeat (8) begin
            out_a_p = (temp & 16'h8000) != 0;
            temp = temp << 1;
            out_b_p = (temp & 16'h8000) != 0;
            temp = temp << 1;
            #(DCO_CLK_PERIOD / 2.0);
        end
    end

    //------------------------------------------------------------------------
    //  Handle the power on Reset
    //------------------------------------------------------------------------
    reg reset = 1;
    initial begin
        if ($test$plusargs("vcd")) begin
            $dumpfile("IserdesSp6.vcd");
            $dumpvars(5, IserdesSp6_tb);
        end
        repeat (3) @(posedge sys_clk);
        reset <= 0;
        #5000
        $finish();
    end
    integer cc = 0;
    always @(posedge sys_clk) cc <= cc + 1;


    //------------------------------------------------------------------------
    //  DUT
    //------------------------------------------------------------------------
    reg bitslip = 0;
    wire sample_clk, dco2x_clk;
    top dut (
        .dco_p          (dco_clk_p),
        .dco_n          (~dco_clk_p),
        .lvds_data_p    ({out_b_p, out_a_p}),
        .lvds_data_n    ({~out_b_p, ~out_a_p}),
        .data_outs      (),
        .data_outs_1    (),
        .bitslip        (bitslip),
        .sample_clk     (sample_clk),
        .dco2x_clk      (dco2x_clk)
    );

    always @(posedge sample_clk) begin
        bitslip <= 0;
        // if ((cc % 20) == 0) bitslip <= 1;
        if (cc == 100) bitslip <= 1;
    end
endmodule