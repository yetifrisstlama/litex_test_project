"""
AD9174-FMC-EBZ board on VC707

See if we can receive a 128 MHz clock from
HMC7044 through the FMC (on GBTCLK0_M2C)

Demonstrate by blinking a LED

try:
  python3 gl_test.py <build / synth / config>
"""
from migen import *
from migen.genlib.io import CRG
from migen.genlib.resetsync import AsyncResetSynchronizer
from litex.build.generic_platform import Subsignal, Pins, IOStandard, Misc
from litex.soc.cores import dna, uart, spi
from litex.soc.interconnect.csr import AutoCSR
from litex.soc.integration.soc_core import SoCCore, csr_map_update
from xdc import vc707
from sys import path
path.append("..")
from common import main


class GtTest(SoCCore, AutoCSR):
    # Peripherals CSR declaration
    csr_peripherals = [
        "dna",
        "spi"
    ]
    csr_map_update(SoCCore.csr_map, csr_peripherals)

    def __init__(self, p, **kwargs):
        print("GtTest: ", p, kwargs)

        # ----------------------------
        #  Litex config
        # ----------------------------
        SoCCore.__init__(
            self,
            clk_freq=int(1e9 / p.default_clk_period),
            cpu_type=None,
            csr_data_width=32,
            with_uart=False,
            with_timer=False,
            integrated_rom_size=0,
            integrated_main_ram_size=0,
            integrated_sram_size=0,
            ident="AD9174 + VC707 test", ident_version=True,
            platform=p,
            **kwargs
        )
        self.submodules += CRG(p.request(p.default_clk_name))

        # ----------------------------
        #  Ports
        # ----------------------------
        p.add_extension([
            ("AD9174_SERDES", 0,
                Subsignal("clk_p", Pins("FMC1_HPC:GBTCLK0_M2C_C_P")),
                Subsignal("clk_n", Pins("FMC1_HPC:GBTCLK0_M2C_C_N")),
            ),
            ("AD9174_SPI", 0,
                # FMC_CS1 (AD9174), FMC_CS2 (HMC7044)
                Subsignal("cs_n", Pins("FMC1_HPC:LA04_N FMC1_HPC:LA05_P")),
                Subsignal("miso", Pins("FMC1_HPC:LA04_P"), Misc("PULLUP TRUE")),
                Subsignal("mosi", Pins("FMC1_HPC:LA03_N")),
                Subsignal("clk",  Pins("FMC1_HPC:LA03_P")),
                Subsignal("spi_en", Pins("FMC1_HPC:LA05_N")),
                IOStandard("LVCMOS18")
            ),
        ])

        # ----------------------------
        #  Clock blinkers
        # ----------------------------
        self.clock_domains.dsp = ClockDomain("dsp")
        self.specials += AsyncResetSynchronizer(self.dsp, ResetSignal('sys'))
        serd_pads = p.request("AD9174_SERDES")
        self.specials += Instance(
            "IBUFDS_GTE2",
            i_CEB=0,
            i_I=serd_pads.clk_p,
            i_IB=serd_pads.clk_n,
            o_O=ClockSignal('dsp')
        )

        # 156.25 MHz / 2**26 = 2.33 Hz
        counter0 = Signal(26)
        self.sync += counter0.eq(counter0 + 1)
        self.comb += p.request("user_led").eq(counter0[-1])

        # 125.00 MHz / 2**26 = 1.86 Hz
        counter1 = Signal(26)
        self.sync.dsp += counter1.eq(counter1 + 1)
        self.comb += p.request("user_led").eq(counter1[-1])

        # ----------------------------
        #  SPI master
        # ----------------------------
        spi_pads = p.request("AD9174_SPI")
        self.comb += spi_pads.spi_en.eq(0)
        self.submodules.spi = spi.SPIMaster(
            spi_pads,
            16,
            self.clk_freq,
            int(1e6)
        )

        # ----------------------------
        #  Serial to Wishbone bridge
        # ----------------------------
        self.add_cpu(uart.UARTWishboneBridge(
            p.request("serial"),
            self.clk_freq,
            baudrate=1152000
        ))
        self.add_wb_master(self.cpu.wishbone)

        # FPGA identification
        self.submodules.dna = dna.DNA()


if __name__ == '__main__':
    soc = GtTest(vc707.Platform())
    main(soc, doc=__doc__)