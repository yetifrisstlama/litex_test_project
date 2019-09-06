# This file is Copyright (c) 2019 Michael Betz <michibetz@gmail.com>
# (Semi-)auto-generated by `python3 gen_vc707.py VC707_rev_2.0.ucf.xdc`

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs -------------------------------------------------------------------------

_io = [
    ("eth", 0,
        Subsignal("rst_n", Pins("AJ33"), IOStandard("LVCMOS18")),
        Subsignal("int_n", Pins("AL31"), IOStandard("LVCMOS18")),
        Subsignal("mdio", Pins("AK33"), IOStandard("LVCMOS18")),
        Subsignal("mdc", Pins("AH31"), IOStandard("LVCMOS18")),
        Subsignal("rx_p", Pins("AM8")),
        Subsignal("rx_n", Pins("AM7")),
        Subsignal("tx_p", Pins("AN2")),
        Subsignal("tx_n", Pins("AN1")),
    ),
    ("sgmii_clock", 0,
        Subsignal("p", Pins("AH8")),
        Subsignal("n", Pins("AH7")),
    ),
    ("pcie_x1", 0,
        Subsignal("rst_n", Pins("AV35"), IOStandard("LVCMOS18")),
        Subsignal("clk_p", Pins("AB8")),
        Subsignal("clk_n", Pins("AB7")),
        Subsignal("rx_p", Pins("Y4")),
        Subsignal("rx_n", Pins("Y3")),
        Subsignal("tx_p", Pins("W2")),
        Subsignal("tx_n", Pins("W1")),
    ),
    ("pcie_x2", 0,
        Subsignal("rst_n", Pins("AV35"), IOStandard("LVCMOS18")),
        Subsignal("clk_p", Pins("AB8")),
        Subsignal("clk_n", Pins("AB7")),
        Subsignal("rx_p", Pins("Y4 AA6")),
        Subsignal("rx_n", Pins("Y3 AA5")),
        Subsignal("tx_p", Pins("W2 AA2")),
        Subsignal("tx_n", Pins("W1 AA1")),
    ),
    ("pcie_x4", 0,
        Subsignal("rst_n", Pins("AV35"), IOStandard("LVCMOS18")),
        Subsignal("clk_p", Pins("AB8")),
        Subsignal("clk_n", Pins("AB7")),
        Subsignal("rx_p", Pins("Y4 AA6 AB4 AC6")),
        Subsignal("rx_n", Pins("Y3 AA5 AB3 AC5")),
        Subsignal("tx_p", Pins("W2 AA2 AC2 AE2")),
        Subsignal("tx_n", Pins("W1 AA1 AC1 AE1")),
    ),
    ("pcie_x8", 0,
        Subsignal("rst_n", Pins("AV35"), IOStandard("LVCMOS18")),
        Subsignal("clk_p", Pins("AB8")),
        Subsignal("clk_n", Pins("AB7")),
        Subsignal("rx_p", Pins("Y4 AA6 AB4 AC6 AD4 AE6 AF4 AG6")),
        Subsignal("rx_n", Pins("Y3 AA5 AB3 AC5 AD3 AE5 AF3 AG5")),
        Subsignal("tx_p", Pins("W2 AA2 AC2 AE2 AG2 AH4 AJ2 AK4")),
        Subsignal("tx_n", Pins("W1 AA1 AC1 AE1 AG1 AH3 AJ1 AK3")),
    ),
    ("clk200", 0,
        Subsignal("p", Pins("E19"), IOStandard("LVDS")),
        Subsignal("n", Pins("E18"), IOStandard("LVDS")),
    ),
    ("clk156", 0,
        Subsignal("p", Pins("AK34"), IOStandard("LVDS")),
        Subsignal("n", Pins("AL34"), IOStandard("LVDS")),
    ),
    ("user_sma_clock", 0,
        Subsignal("p", Pins("AJ32"), IOStandard("LVCMOS18")),
        Subsignal("n", Pins("AK32"), IOStandard("LVCMOS18")),
    ),
    ("user_sma_mgt_refclk", 0,
        Subsignal("p", Pins("AK8")),
        Subsignal("n", Pins("AK7")),
    ),
    ("user_sma_mgt_rx", 0,
        Subsignal("p", Pins("AN6")),
        Subsignal("n", Pins("AN5")),
    ),
    ("user_sma_mgt_tx", 0,
        Subsignal("p", Pins("AP4")),
        Subsignal("n", Pins("AP3")),
    ),
    ("si5324", 0,
        Subsignal("rst_n", Pins("AT36"), IOStandard("LVCMOS18")),
        Subsignal("int", Pins("AU34"), IOStandard("LVCMOS18")),
    ),
    ("si5324_clkin", 0,
        Subsignal("p", Pins("AD8")),
        Subsignal("n", Pins("AD7")),
    ),
    ("cpu_reset", 0, Pins("AV40"), IOStandard("LVCMOS18")),
    ("user_led", 0, Pins("AM39"), IOStandard("LVCMOS18")),
    ("user_led", 1, Pins("AN39"), IOStandard("LVCMOS18")),
    ("user_led", 2, Pins("AR37"), IOStandard("LVCMOS18")),
    ("user_led", 3, Pins("AT37"), IOStandard("LVCMOS18")),
    ("user_led", 4, Pins("AR35"), IOStandard("LVCMOS18")),
    ("user_led", 5, Pins("AP41"), IOStandard("LVCMOS18")),
    ("user_led", 6, Pins("AP42"), IOStandard("LVCMOS18")),
    ("user_led", 7, Pins("AU39"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 0, Pins("AV30"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 1, Pins("AY33"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 2, Pins("BA31"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 3, Pins("BA32"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 4, Pins("AW30"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 5, Pins("AY30"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 6, Pins("BA30"), IOStandard("LVCMOS18")),
    ("user_dip_btn", 7, Pins("BB31"), IOStandard("LVCMOS18")),
    ("user_btn_c", 0, Pins("AV39"), IOStandard("LVCMOS18")),
    ("user_btn_n", 0, Pins("AR40"), IOStandard("LVCMOS18")),
    ("user_btn_e", 0, Pins("AU38"), IOStandard("LVCMOS18")),
    ("user_btn_s", 0, Pins("AP40"), IOStandard("LVCMOS18")),
    ("user_btn_w", 0, Pins("AW40"), IOStandard("LVCMOS18")),
    ("rotary", 0,
        Subsignal("a", Pins("AR33"), IOStandard("LVCMOS18")),
        Subsignal("b", Pins("AT31"), IOStandard("LVCMOS18")),
        Subsignal("push", Pins("AW31"), IOStandard("LVCMOS18")),
    ),
    ("user_sma_gpio_p", 0, Pins("AN31"), IOStandard("LVCMOS18")),
    ("user_sma_gpio_n", 0, Pins("AP31"), IOStandard("LVCMOS18")),
    ("lcd", 0,
        Subsignal("db", Pins("AT42 AR38 AR39 AN40"), IOStandard("LVCMOS18")),
        Subsignal("rs", Pins("AN41"), IOStandard("LVCMOS18")),
        Subsignal("rw", Pins("AR42"), IOStandard("LVCMOS18")),
        Subsignal("e", Pins("AT40"), IOStandard("LVCMOS18")),
    ),
    ("i2c", 0,
        Subsignal("scl", Pins("AT35"), IOStandard("LVCMOS18")),
        Subsignal("sda", Pins("AU32"), IOStandard("LVCMOS18")),
    ),
    ("i2c_mux_reset", 0, Pins("AY42"), IOStandard("LVCMOS18")),
    ("XADC", {
        "GPIO_0": "BA21",
        "GPIO_1": "BB21",
        "GPIO_2": "BB24",
        "GPIO_3": "BB23",
        "VAUX0_N": "AP38",
        "VAUX0_P": "AN38",
        "VAUX8_N": "AM42",
        "VAUX8_P": "AM41",
    }),
    ("serial", 0,
        Subsignal("rx", Pins("AU36"), IOStandard("LVCMOS18")),
        Subsignal("rts", Pins("AT32"), IOStandard("LVCMOS18")),
        Subsignal("tx", Pins("AU33"), IOStandard("LVCMOS18")),
        Subsignal("cts", Pins("AR34"), IOStandard("LVCMOS18")),
    ),
    ("hdmi", 0,
        Subsignal("d", Pins("AM22 AL22 AJ20 AJ21 AM21 AL21 AK22 AJ22 AL20 AK20 AK23 AJ23 AN21 AP22 AP23 AN23 AM23 AN24 AY24 BB22 BA22 BA25 AY25 AY22 AY23 AV24 AU24 AW21 AV21 AT24 AR24 AU21 AT21 AW22 AW23 AV23"), IOStandard("LVCMOS18")),
        Subsignal("de", Pins("AP21"), IOStandard("LVCMOS18")),
        Subsignal("clk", Pins("AU23"), IOStandard("LVCMOS18")),
        Subsignal("vsync", Pins("AT22"), IOStandard("LVCMOS18")),
        Subsignal("hsync", Pins("AU22"), IOStandard("LVCMOS18")),
        Subsignal("int", Pins("AM24"), IOStandard("LVCMOS18")),
        Subsignal("spdif", Pins("AR23"), IOStandard("LVCMOS18")),
        Subsignal("spdif_out", Pins("AR22"), IOStandard("LVCMOS18")),
    ),
    ("ddram", 0,
        Subsignal("a", Pins("A20 B19 C20 A19 A17 A16 D20 C18 D17 C19 B21 B17 A15 A21 F17 E17"), IOStandard("SSTL15")),
        Subsignal("ba", Pins("D21 C21 D18"), IOStandard("SSTL15")),
        Subsignal("ras_n", Pins("E20"), IOStandard("SSTL15")),
        Subsignal("cas_n", Pins("K17"), IOStandard("SSTL15")),
        Subsignal("we_n", Pins("F20"), IOStandard("SSTL15")),
        Subsignal("cs_n", Pins("J17"), IOStandard("SSTL15")),
        Subsignal("dm", Pins("M13 K15 F12 A14 C23 D25 C31 F31"), IOStandard("SSTL15")),
        Subsignal("dq", Pins("N14 N13 L14 M14 M12 N15 M11 L12 K14 K13 H13 J13 L16 L15 H14 J15 E15 E13 F15 E14 G13 G12 F14 G14 B14 C13 B16 D15 D13 E12 C16 D16 A24 B23 B27 B26 A22 B22 A25 C24 E24 D23 D26 C25 E23 D22 F22 E22 A30 D27 A29 C28 D28 B31 A31 A32 E30 F29 F30 F27 C30 E29 F26 D30"), IOStandard("SSTL15")),
        Subsignal("dqs_p", Pins("N16 K12 H16 C15 A26 F25 B28 E27"), IOStandard("DIFF_SSTL15")),
        Subsignal("dqs_n", Pins("M16 J12 G16 C14 A27 E25 B29 E28"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_p", Pins("H19"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_n", Pins("G18"), IOStandard("DIFF_SSTL15")),
        Subsignal("cke", Pins("K19"), IOStandard("SSTL15")),
        Subsignal("odt", Pins("H20"), IOStandard("SSTL15")),
        Subsignal("reset_n", Pins("C29"), IOStandard("LVCMOS15")),
    ),
    ("ddram_dual_rank", 0,
        Subsignal("a", Pins("A20 B19 C20 A19 A17 A16 D20 C18 D17 C19 B21 B17 A15 A21 F17 E17"), IOStandard("SSTL15")),
        Subsignal("ba", Pins("D21 C21 D18"), IOStandard("SSTL15")),
        Subsignal("ras_n", Pins("E20"), IOStandard("SSTL15")),
        Subsignal("cas_n", Pins("K17"), IOStandard("SSTL15")),
        Subsignal("we_n", Pins("F20"), IOStandard("SSTL15")),
        Subsignal("cs_n", Pins("J17 J20"), IOStandard("SSTL15")),
        Subsignal("dm", Pins("M13 K15 F12 A14 C23 D25 C31 F31"), IOStandard("SSTL15")),
        Subsignal("dq", Pins("N14 N13 L14 M14 M12 N15 M11 L12 K14 K13 H13 J13 L16 L15 H14 J15 E15 E13 F15 E14 G13 G12 F14 G14 B14 C13 B16 D15 D13 E12 C16 D16 A24 B23 B27 B26 A22 B22 A25 C24 E24 D23 D26 C25 E23 D22 F22 E22 A30 D27 A29 C28 D28 B31 A31 A32 E30 F29 F30 F27 C30 E29 F26 D30"), IOStandard("SSTL15")),
        Subsignal("dqs_p", Pins("N16 K12 H16 C15 A26 F25 B28 E27"), IOStandard("DIFF_SSTL15")),
        Subsignal("dqs_n", Pins("M16 J12 G16 C14 A27 E25 B29 E28"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_p", Pins("H19 G19"), IOStandard("DIFF_SSTL15")),
        Subsignal("clk_n", Pins("G18 F19"), IOStandard("DIFF_SSTL15")),
        Subsignal("cke", Pins("K19 J18"), IOStandard("SSTL15")),
        Subsignal("odt", Pins("H20 H18"), IOStandard("SSTL15")),
        Subsignal("reset_n", Pins("C29"), IOStandard("LVCMOS15")),
    ),
    ("sfp", 0,
        Subsignal("txp", Pins("AM4")),
        Subsignal("txn", Pins("AM3")),
        Subsignal("rxp", Pins("AL6")),
        Subsignal("rxn", Pins("AL5")),
    ),
    ("sfp_tx", 0,
        Subsignal("txp", Pins("AM4")),
        Subsignal("txn", Pins("AM3")),
    ),
    ("sfp_rx", 0,
        Subsignal("rxp", Pins("AL6")),
        Subsignal("rxn", Pins("AL5")),
    ),
    ("sfp_tx_disable_n", 0, Pins("AP33"), IOStandard("LVCMOS18")),
    ("sfp_rx_los", 0, Pins("BB38"), IOStandard("LVCMOS18")),
    ("mmc", 0,
        Subsignal("clk", Pins("AN30"), IOStandard("LVCMOS18")),
        Subsignal("cmd", Pins("AP30"), IOStandard("LVCMOS18")),
        Subsignal("det", Pins("AP32"), IOStandard("LVCMOS18")),
        Subsignal("wp", Pins("AR32"), IOStandard("LVCMOS18")),
        Subsignal("dat", Pins("AR30 AU31 AV31 AT30"), IOStandard("LVCMOS18")),
    ),
    ("vadj_on_b", 0, Pins("AH35"), IOStandard("LVCMOS18")),
]

# Connectors ------------------------------------------------------------------

_connectors = [
    ("FMC1_HPC", {
        "CLK0_M2C_N": "L40",
        "CLK0_M2C_P": "L39",
        "CLK1_M2C_N": "M31",
        "CLK1_M2C_P": "N30",
        "DP0_C2M_N": "E1",
        "DP0_C2M_P": "E2",
        "DP0_M2C_N": "D7",
        "DP0_M2C_P": "D8",
        "DP1_C2M_N": "D3",
        "DP1_C2M_P": "D4",
        "DP1_M2C_N": "C5",
        "DP1_M2C_P": "C6",
        "DP2_C2M_N": "C1",
        "DP2_C2M_P": "C2",
        "DP2_M2C_N": "B7",
        "DP2_M2C_P": "B8",
        "DP3_C2M_N": "B3",
        "DP3_C2M_P": "B4",
        "DP3_M2C_N": "A5",
        "DP3_M2C_P": "A6",
        "DP4_C2M_N": "J1",
        "DP4_C2M_P": "J2",
        "DP4_M2C_N": "H7",
        "DP4_M2C_P": "H8",
        "DP5_C2M_N": "H3",
        "DP5_C2M_P": "H4",
        "DP5_M2C_N": "G5",
        "DP5_M2C_P": "G6",
        "DP6_C2M_N": "G1",
        "DP6_C2M_P": "G2",
        "DP6_M2C_N": "F7",
        "DP6_M2C_P": "F8",
        "DP7_C2M_N": "F3",
        "DP7_C2M_P": "F4",
        "DP7_M2C_N": "E5",
        "DP7_M2C_P": "E6",
        "GBTCLK0_M2C_C_N": "A9",
        "GBTCLK0_M2C_C_P": "A10",
        "GBTCLK1_M2C_C_N": "E9",
        "GBTCLK1_M2C_C_P": "E10",
        "HA00_CC_N": "E35",
        "HA00_CC_P": "E34",
        "HA01_CC_N": "D36",
        "HA01_CC_P": "D35",
        "HA02_N": "D33",
        "HA02_P": "E33",
        "HA03_N": "G33",
        "HA03_P": "H33",
        "HA04_N": "F35",
        "HA04_P": "F34",
        "HA05_N": "F32",
        "HA05_P": "G32",
        "HA06_N": "G37",
        "HA06_P": "G36",
        "HA07_N": "C39",
        "HA07_P": "C38",
        "HA08_N": "H36",
        "HA08_P": "J36",
        "HA09_N": "D32",
        "HA09_P": "E32",
        "HA10_N": "G38",
        "HA10_P": "H38",
        "HA11_N": "J38",
        "HA11_P": "J37",
        "HA12_N": "B38",
        "HA12_P": "B37",
        "HA13_N": "A37",
        "HA13_P": "B36",
        "HA14_N": "E38",
        "HA14_P": "E37",
        "HA15_N": "C34",
        "HA15_P": "C33",
        "HA16_N": "A39",
        "HA16_P": "B39",
        "HA17_CC_N": "C36",
        "HA17_CC_P": "C35",
        "HA18_N": "E39",
        "HA18_P": "F39",
        "HA19_N": "B33",
        "HA19_P": "B32",
        "HA20_N": "A34",
        "HA20_P": "B34",
        "HA21_N": "D38",
        "HA21_P": "D37",
        "HA22_N": "F37",
        "HA22_P": "F36",
        "HA23_N": "A36",
        "HA23_P": "A35",
        "HB00_CC_N": "J26",
        "HB00_CC_P": "J25",
        "HB01_N": "H29",
        "HB01_P": "H28",
        "HB02_N": "J28",
        "HB02_P": "K28",
        "HB03_N": "G29",
        "HB03_P": "G28",
        "HB04_N": "G24",
        "HB04_P": "H24",
        "HB05_N": "J27",
        "HB05_P": "K27",
        "HB06_CC_N": "J23",
        "HB06_CC_P": "K23",
        "HB07_N": "G27",
        "HB07_P": "G26",
        "HB08_N": "H26",
        "HB08_P": "H25",
        "HB09_N": "G23",
        "HB09_P": "H23",
        "HB10_N": "L22",
        "HB10_P": "M22",
        "HB11_N": "J22",
        "HB11_P": "K22",
        "HB12_N": "K25",
        "HB12_P": "K24",
        "HB13_N": "P26",
        "HB13_P": "P25",
        "HB14_N": "H21",
        "HB14_P": "J21",
        "HB15_N": "L21",
        "HB15_P": "M21",
        "HB16_N": "N26",
        "HB16_P": "N25",
        "HB17_CC_N": "L24",
        "HB17_CC_P": "M24",
        "HB18_N": "G22",
        "HB18_P": "G21",
        "HB19_N": "L26",
        "HB19_P": "L25",
        "HB20_N": "N21",
        "HB20_P": "P21",
        "HB21_N": "P23",
        "HB21_P": "P22",
        "LA00_CC_N": "K40",
        "LA00_CC_P": "K39",
        "LA01_CC_N": "J41",
        "LA01_CC_P": "J40",
        "LA02_N": "N41",
        "LA02_P": "P41",
        "LA03_N": "L42",
        "LA03_P": "M42",
        "LA04_N": "H41",
        "LA04_P": "H40",
        "LA05_N": "L41",
        "LA05_P": "M41",
        "LA06_N": "J42",
        "LA06_P": "K42",
        "LA07_N": "G42",
        "LA07_P": "G41",
        "LA08_N": "M38",
        "LA08_P": "M37",
        "LA09_N": "P42",
        "LA09_P": "R42",
        "LA10_N": "M39",
        "LA10_P": "N38",
        "LA11_N": "F41",
        "LA11_P": "F40",
        "LA12_N": "P40",
        "LA12_P": "R40",
        "LA13_N": "G39",
        "LA13_P": "H39",
        "LA14_N": "N40",
        "LA14_P": "N39",
        "LA15_N": "L37",
        "LA15_P": "M36",
        "LA16_N": "K38",
        "LA16_P": "K37",
        "LA17_CC_N": "K32",
        "LA17_CC_P": "L31",
        "LA18_CC_N": "L32",
        "LA18_CC_P": "M32",
        "LA19_N": "W31",
        "LA19_P": "W30",
        "LA20_N": "Y30",
        "LA20_P": "Y29",
        "LA21_N": "N29",
        "LA21_P": "N28",
        "LA22_N": "P28",
        "LA22_P": "R28",
        "LA23_N": "N31",
        "LA23_P": "P30",
        "LA24_N": "P31",
        "LA24_P": "R30",
        "LA25_N": "K30",
        "LA25_P": "K29",
        "LA26_N": "H30",
        "LA26_P": "J30",
        "LA27_N": "H31",
        "LA27_P": "J31",
        "LA28_N": "L30",
        "LA28_P": "L29",
        "LA29_N": "T30",
        "LA29_P": "T29",
        "LA30_N": "V31",
        "LA30_P": "V30",
        "LA31_N": "M29",
        "LA31_P": "M28",
        "LA32_N": "U29",
        "LA32_P": "V29",
        "LA33_N": "T31",
        "LA33_P": "U31",
        "PG_M2C_LS": "AN34",
        "PRSNT_M2C_B_LS": "AM31",
    }),
    ("FMC2_HPC", {
        "CLK0_M2C_N": "AF40",
        "CLK0_M2C_P": "AF39",
        "CLK1_M2C_N": "T39",
        "CLK1_M2C_P": "U39",
        "DP0_C2M_N": "N1",
        "DP0_C2M_P": "N2",
        "DP0_M2C_N": "P7",
        "DP0_M2C_P": "P8",
        "DP1_C2M_N": "M3",
        "DP1_C2M_P": "M4",
        "DP1_M2C_N": "N5",
        "DP1_M2C_P": "N6",
        "DP2_C2M_N": "L1",
        "DP2_C2M_P": "L2",
        "DP2_M2C_N": "L5",
        "DP2_M2C_P": "L6",
        "DP3_C2M_N": "K3",
        "DP3_C2M_P": "K4",
        "DP3_M2C_N": "J5",
        "DP3_M2C_P": "J6",
        "DP4_C2M_N": "U1",
        "DP4_C2M_P": "U2",
        "DP4_M2C_N": "W5",
        "DP4_M2C_P": "W6",
        "DP5_C2M_N": "T3",
        "DP5_C2M_P": "T4",
        "DP5_M2C_N": "V3",
        "DP5_M2C_P": "V4",
        "DP6_C2M_N": "R1",
        "DP6_C2M_P": "R2",
        "DP6_M2C_N": "U5",
        "DP6_M2C_P": "U6",
        "DP7_C2M_N": "P3",
        "DP7_C2M_P": "P4",
        "DP7_M2C_N": "R5",
        "DP7_M2C_P": "R6",
        "GBTCLK0_M2C_C_N": "K7",
        "GBTCLK0_M2C_C_P": "K8",
        "GBTCLK1_M2C_C_N": "T7",
        "GBTCLK1_M2C_C_P": "T8",
        "HA00_CC_N": "AC33",
        "HA00_CC_P": "AB33",
        "HA01_CC_N": "AD33",
        "HA01_CC_P": "AD32",
        "HA02_N": "AD30",
        "HA02_P": "AC30",
        "HA03_N": "AA30",
        "HA03_P": "AA29",
        "HA04_N": "AC29",
        "HA04_P": "AB29",
        "HA05_N": "Y33",
        "HA05_P": "Y32",
        "HA06_N": "AB32",
        "HA06_P": "AB31",
        "HA07_N": "AD31",
        "HA07_P": "AC31",
        "HA08_N": "AA32",
        "HA08_P": "AA31",
        "HA09_N": "AE30",
        "HA09_P": "AE29",
        "HA10_N": "AF32",
        "HA10_P": "AF31",
        "HA11_N": "AE35",
        "HA11_P": "AE34",
        "HA12_N": "AG34",
        "HA12_P": "AF34",
        "HA13_N": "AE33",
        "HA13_P": "AE32",
        "HA14_N": "AF36",
        "HA14_P": "AF35",
        "HA15_N": "AF37",
        "HA15_P": "AE37",
        "HA16_N": "AH36",
        "HA16_P": "AG36",
        "HA17_CC_N": "AD35",
        "HA17_CC_P": "AC34",
        "HA18_N": "AB37",
        "HA18_P": "AB36",
        "HA19_N": "AC36",
        "HA19_P": "AC35",
        "HA20_N": "AD37",
        "HA20_P": "AD36",
        "HA21_N": "AA35",
        "HA21_P": "AA34",
        "HA22_N": "AA36",
        "HA22_P": "Y35",
        "HA23_N": "AA37",
        "HA23_P": "Y37",
        "LA00_CC_N": "AD41",
        "LA00_CC_P": "AD40",
        "LA01_CC_N": "AG41",
        "LA01_CC_P": "AF41",
        "LA02_N": "AL39",
        "LA02_P": "AK39",
        "LA03_N": "AK42",
        "LA03_P": "AJ42",
        "LA04_N": "AL42",
        "LA04_P": "AL41",
        "LA05_N": "AG42",
        "LA05_P": "AF42",
        "LA06_N": "AE38",
        "LA06_P": "AD38",
        "LA07_N": "AC41",
        "LA07_P": "AC40",
        "LA08_N": "AE42",
        "LA08_P": "AD42",
        "LA09_N": "AK38",
        "LA09_P": "AJ38",
        "LA10_N": "AB42",
        "LA10_P": "AB41",
        "LA11_N": "AA42",
        "LA11_P": "Y42",
        "LA12_N": "AA39",
        "LA12_P": "Y39",
        "LA13_N": "Y40",
        "LA13_P": "W40",
        "LA14_N": "AB39",
        "LA14_P": "AB38",
        "LA15_N": "AC39",
        "LA15_P": "AC38",
        "LA16_N": "AJ41",
        "LA16_P": "AJ40",
        "LA17_CC_N": "U38",
        "LA17_CC_P": "U37",
        "LA18_CC_N": "T37",
        "LA18_CC_P": "U36",
        "LA19_N": "U33",
        "LA19_P": "U32",
        "LA20_N": "V34",
        "LA20_P": "V33",
        "LA21_N": "P36",
        "LA21_P": "P35",
        "LA22_N": "W33",
        "LA22_P": "W32",
        "LA23_N": "R39",
        "LA23_P": "R38",
        "LA24_N": "T35",
        "LA24_P": "U34",
        "LA25_N": "R34",
        "LA25_P": "R33",
        "LA26_N": "N34",
        "LA26_P": "N33",
        "LA27_N": "P33",
        "LA27_P": "P32",
        "LA28_N": "V36",
        "LA28_P": "V35",
        "LA29_N": "W37",
        "LA29_P": "W36",
        "LA30_N": "R32",
        "LA30_P": "T32",
        "LA31_N": "V40",
        "LA31_P": "V39",
        "LA32_N": "P38",
        "LA32_P": "P37",
        "LA33_N": "R37",
        "LA33_P": "T36",
        "PG_M2C_LS": "AF29",
        "PRSNT_M2C_B_LS": "AG32",
    }),
]

# Platform --------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name = "clk156"
    default_clk_period = 1e9 / 156.25e6

    def __init__(self):
        XilinxPlatform.__init__(
            self,
            "xc7vx485tffg1761-2",
            _io,
            _connectors,
            toolchain="vivado"
        )
        self.add_platform_command("""
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 2.5 [current_design]
""")

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        try:
            self.add_period_constraint(
                self.lookup_request("clk200").p,
                1e9 / 200e6
            )
        except ConstraintError:
            pass
        try:
            self.add_period_constraint(
                self.lookup_request("sgmii_clock").p,
                1e9 / 125e6
            )
        except ConstraintError:
            pass
