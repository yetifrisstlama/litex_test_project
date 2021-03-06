`timescale 1 ns / 1 ns

module basesoc_kc705_tb;
    localparam real XTAL_PERIOD = 1e9 / 156e6;    // System clock period in [ns]
    localparam real RX_CLK_PERIOD = 1e9 / 125e6;  // PHY RX clock

    //------------------------------------------------------------------------
    // Clock and fake LVDS lanes generation
    //------------------------------------------------------------------------
    reg xtal_clk = 1;
    reg eth_clocks_rx = 1;
    always #(XTAL_PERIOD / 2) xtal_clk = ~xtal_clk;
    always #(RX_CLK_PERIOD / 2) eth_clocks_rx = ~eth_clocks_rx;

    //------------------------------------------------------------------------
    //  Handle the power on Reset
    //------------------------------------------------------------------------
    reg reset = 1;
    initial begin
        if ($test$plusargs("vcd")) begin
            $dumpfile("basesoc_kc705.vcd");
            $dumpvars(5, basesoc_kc705_tb);
        end
        repeat (3) @(posedge xtal_clk);
        reset <= 0;
        #5000
        $finish();
    end

    //------------------------------------------------------------------------
    //  DUT
    //------------------------------------------------------------------------
    integer cc = 0;
    integer i = 0;
    wire eth_clocks_gtx, eth_tx_en, eth_rst_n;
    wire [7:0] eth_tx_data;
    reg [7:0] eth_rx_data = 0;
    reg eth_rx_dv = 0;
    reg [7:0] ethData [69:0];
    initial $readmemh("arp_req.hex", ethData);
    always @(posedge eth_clocks_gtx) begin
        if (eth_rst_n == 0) begin
            cc <= 0;
            i <= 0;
            eth_rx_dv <= 0;
            eth_rx_data <= 0;
        end else begin
            cc <= cc + 1;
            eth_rx_dv <= 1'b0;
            if (cc > 10 && i < 70) begin
                i <= i + 1;
                eth_rx_dv <= 1'b1;
                eth_rx_data <= ethData[i];
            end
        end
    end

    basesoc_kc705 dut (
        .serial_cts     (1'b0),
        .serial_rts     (1'b0),
        .serial_rx      (1'b0),
        .clk156_p       (xtal_clk),
        .clk156_n       (~xtal_clk),
        .eth_int_n      (1'b0),            // Not used
        .eth_rx_er      (1'b0),            // not used
        .eth_col        (1'b0),            // Collision (not used)
        .eth_crs        (1'b0),            // Carrier sense (not used)
        .eth_rx_dv      (eth_rx_dv),
        .eth_rx_data    (eth_rx_data),     // from phy to fpga
        .eth_clocks_rx  (eth_clocks_rx),   // from phy (cable) to FPGA
        .eth_clocks_gtx (eth_clocks_gtx),  // from FPGA to PHY
        .eth_tx_data    (eth_tx_data),
        .eth_tx_en      (eth_tx_en),
        .eth_rst_n      (eth_rst_n)        // Reset phy
    );

endmodule

