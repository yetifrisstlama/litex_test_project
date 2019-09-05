'''
generates vc707.py litex platform file

usage:
$ python3 gen_vc707.py > vc707.py

needs master .xdc file from xilinx:
https://www.xilinx.com/member/forms/download/design-license.html?cid=203195&filename=vc707-ucf-xdc-rdf0155-rev2-0.zip

c59a0b33fb1c0369600fa35169e463742a48a65d9bf884238cf3101ee0ace6e2  VC707_rev_2.0.ucf.xdc
'''
from xdc_parser import XdcParser

p = XdcParser('./VC707_rev_2.0.ucf.xdc')

print('''\
# This file is Copyright (c) 2019 Michael Betz <michibetz@gmail.com>

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform, VivadoProgrammer

# IOs ----------------------------------------------------------------------------------------------

_io = [
''', end='')

p.getGroup('eth', (
    ('rst_n', 'PHY_RESET_LS'),
    ('int_n', 'PHY_INT_LS'),
    ('mdio', 'PHY_MDIO_LS'),
    ('mdc', 'PHY_MDC_LS'),
    ('rx_p', 'SGMII_RX_P'),
    ('rx_n', 'SGMII_RX_N'),
    ('tx_p', 'SGMII_TX_P'),
    ('tx_n', 'SGMII_TX_N'),
))
p.getGroup('sgmii_clock', (
    ('p', 'SGMIICLK_Q0_P'),
    ('n', 'SGMIICLK_Q0_N'),
))

for i in [1, 2, 4, 8]:
    p.getGroup('pcie_x{:}'.format(i), (
        ('rst_n', 'PCIE_PERST_.*'),
        ('clk_p', 'PCIE_CLK_QO_P'),
        ('clk_n', 'PCIE_CLK_QO_N'),
        ('rx_p', 'PCIE_RX[0-7]_P', i),
        ('rx_n', 'PCIE_RX[0-7]_N', i),
        ('tx_p', 'PCIE_TX[0-7]_P', i),
        ('tx_n', 'PCIE_TX[0-7]_N', i),
    ))

p.getGroup('clk200', (
    ('p', 'SYSCLK_P'),
    ('n', 'SYSCLK_N'),
))
p.getGpios('user_sma_clock_p', 'USER_SMA_CLOCK_P')
p.getGpios('user_sma_clock_n', 'USER_SMA_CLOCK_N')
p.getGroup('user_sma_clock', (
    ('p', 'USER_SMA_CLOCK_P'),
    ('n', 'USER_SMA_CLOCK_N'),
))
p.getGpios('user_clock_p', 'USER_CLOCK_P')
p.getGpios('user_clock_n', 'USER_CLOCK_N')
p.getGroup('user_sma_mgt_tx', (
    ('p', 'SMA_MGT_TX_P'),
    ('n', 'SMA_MGT_TX_N'),
))
p.getGroup('user_sma_mgt_rx', (
    ('p', 'SMA_MGT_RX_P'),
    ('n', 'SMA_MGT_RX_N'),
))
p.getGroup('user_sma_mgt_refclk', (
    ('p', 'SMA_MGT_REFCLK_P'),
    ('n', 'SMA_MGT_REFCLK_N'),
))
p.getGroup('si5324', (
    ('rst_n', 'SI5324_RST_LS'),
    ('int', 'SI5324_INT_ALM_LS'),
))
p.getGroup('si5324_clkin', (
    ('p', 'REC_CLOCK_C_P'),
    ('n', 'REC_CLOCK_C_N'),
))

p.getGpios('cpu_reset', 'CPU_RESET')
p.getGpios('user_led', 'GPIO_LED_[0-9]_LS')
p.getGpios('user_dip_btn', 'GPIO_DIP_SW[0-9]')
p.getGpios('user_btn_c', 'GPIO_SW_C')
p.getGpios('user_btn_n', 'GPIO_SW_N')
p.getGpios('user_btn_e', 'GPIO_SW_E')
p.getGpios('user_btn_s', 'GPIO_SW_S')
p.getGpios('user_btn_w', 'GPIO_SW_W')
p.getGroup('rotary', (
    ('a', 'ROTARY_INCA'),
    ('b', 'ROTARY_INCB'),
    ('push', 'ROTARY_PUSH'),
))
p.getGpios('user_sma_gpio_p', 'USER_SMA_GPIO_P')
p.getGpios('user_sma_gpio_n', 'USER_SMA_GPIO_N')
p.getGroup('lcd', (
    ('db', 'LCD_DB[4-7]_LS'),
    ('rs', 'LCD_RS_LS'),
    ('rw', 'LCD_RW_LS'),
    ('e', 'LCD_E_LS'),
))
p.getGroup('i2c', (
    ('scl', 'IIC_SCL_MAIN_LS'),
    ('sda', 'IIC_SDA_MAIN_LS'),
))
p.getGpios('i2c_mux_reset', 'IIC_MUX_RESET_B_LS')
p.getConnector("XADC", nameReplace=(('N_R', '_N'),('P_R', '_P')))
p.getGroup('serial', (
    ('rx', 'USB_UART_RX'),
    ('rts', 'USB_UART_RTS'),
    ('tx', 'USB_UART_TX'),
    ('cts', 'USB_UART_CTS'),
))

p.getGroup('hdmi', (
    ('d', 'HDMI_R_D\d+', 36),
    ('de', 'HDMI_R_DE'),
    ('clk', 'HDMI_R_CLK'),
    ('vsync', 'HDMI_R_VSYNC'),
    ('hsync', 'HDMI_R_HSYNC'),
    ('int', 'HDMI_INT'),
    ('spdif', 'HDMI_R_SPDIF'),
    ('spdif_out', 'HDMI_SPDIF_OUT_LS')
))

for n, i in (('ddram', 1), ('ddram_dual_rank', 2)):
    p.getGroup(n, (
        ('a', 'DDR3_A\d+', 16),
        ('ba', 'DDR3_BA\d', 3),
        ('ras_n', 'DDR3_RAS_B'),
        ('cas_n', 'DDR3_CAS_B'),
        ('we_n', 'DDR3_WE_B'),
        ('cs_n', 'DDR3_S\d_B', i),  # hope this is right ???
        ('dm', 'DDR3_DM\d', 8),
        ('dq', 'DDR3_D\d+', 64),
        ('dqs_p', 'DDR3_DQS\d_P', 8),
        ('dqs_n', 'DDR3_DQS\d_N', 8),
        ('clk_p', 'DDR3_CLK\d_P', i),
        ('clk_n', 'DDR3_CLK\d_N', i),
        ('cke', 'DDR3_CKE\d', i),
        ('odt', 'DDR3_ODT\d', i),
        ('reset_n', 'DDR3_RESET_B'),
    ))

p.getGroup('sfp', (
    ('txp', 'SFP_TX_P'),
    ('txn', 'SFP_TX_N'),
    ('rxp', 'SFP_RX_P'),
    ('rxn', 'SFP_RX_N')
))
p.getGroup('sfp_tx', (
    ('txp', 'SFP_TX_P'),
    ('txn', 'SFP_TX_N'),
))
p.getGroup('sfp_rx', (
    ('rxp', 'SFP_RX_P'),
    ('rxn', 'SFP_RX_N')
))
p.getGpios('sfp_tx_disable_n', 'SFP_TX_DISABLE')
p.getGpios('sfp_rx_los', 'SFP_LOS_LS')

p.props["SDIO_DAT3_LS"] = p.props["SDIO_CD_DAT3_LS"]
p.sortKeys()
p.getGroup('mmc', (
    ('clk', 'SDIO_CLK_LS'),
    ('cmd', 'SDIO_CMD_LS'),
    ('det', 'SDIO_SDDET'),
    ('wp', 'SDIO_SDWP'),
    ('dat', 'SDIO_DAT[0-3]_LS', 4),
))

p.getGpios('vadj_on_b', 'FMC_VADJ_ON_B_LS')

print('''\
]

# Connectors ---------------------------------------------------------------------------------------

_connectors = [
''', end='')

p.getConnector('FMC1_HPC')
p.getConnector('FMC2_HPC')

print('''\
]

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name = "clk156"
    default_clk_period = 1e9/156.5e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7k325t-ffg900-2", _io, _connectors, toolchain="vivado")
        self.add_platform_command("""
set_property CFGBVS VCCO [current_design]
set_property CONFIG_VOLTAGE 2.5 [current_design]
""")
        self.toolchain.bitstream_commands = ["set_property BITSTREAM.CONFIG.SPI_BUSWIDTH 4 [current_design]"]
        self.toolchain.additional_commands = ["write_cfgmem -force -format bin -interface spix4 -size 16 -loadbit \"up 0x0 {build_name}.bit\" -file {build_name}.bin"]

    def create_programmer(self):
        return VivadoProgrammer()

    def do_finalize(self, fragment):
        XilinxPlatform.do_finalize(self, fragment)
        try:
            self.add_period_constraint(self.lookup_request("clk200").p, 1e9/200e6)
        except ConstraintError:
            pass
        try:
            self.add_period_constraint(self.lookup_request("eth_clocks").rx, 1e9/125e6)
        except ConstraintError:
            pass
        try:
            self.add_period_constraint(self.lookup_request("eth_clocks").tx, 1e9/125e6)
        except ConstraintError:
            pass
        self.add_platform_command("set_property DCI_CASCADE {{32 34}} [get_iobanks 33]")
''', end='')