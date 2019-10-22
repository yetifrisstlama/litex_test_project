"""
Vector voltmeter
"""

from migen import *
from litex.soc.interconnect.csr import AutoCSR, CSRStorage, CSRStatus


class DspWrapper(Module, AutoCSR):
    def __init__(self):
        """
        mems
            list of memory objects of length N_CHANNELS
        acquisition starts after
          * rising edge on self.trigger
          * data_in of the selected channel crossing trig_level
        """
        self.adc_ref = Signal((14, True))
        self.adc_a = Signal((14, True))
        self.adc_b = Signal((14, True))
        self.adc_c = Signal((14, True))

        ###

        self.ddc_ftw = CSRStorage(32, reset=0x40059350)
        self.ddc_deci = CSRStorage(13, reset=48)

        self.mag_ref = CSRStatus(20)
        self.mag_a   = CSRStatus(20)
        self.mag_b   = CSRStatus(20)
        self.mag_c   = CSRStatus(20)

        self.phase_ref = CSRStatus(21)
        self.phase_a   = CSRStatus(21)
        self.phase_b   = CSRStatus(21)
        self.phase_c   = CSRStatus(21)

        self.specials += Instance("dsp",
            i_clk=ClockSignal("sample"),
            i_reset=ResetSignal("sample"),

            i_adc_ref=self.adc_ref,
            i_adc_a=self.adc_a,
            i_adc_b=self.adc_b,
            i_adc_c=self.adc_c,

            o_mag_ref=self.mag_ref.status,
            o_mag_a=self.mag_a.status,
            o_mag_b=self.mag_b.status,
            o_mag_c=self.mag_c.status,

            o_phase_ref=self.phase_ref.status,
            o_phase_a=self.phase_a.status,
            o_phase_b=self.phase_b.status,
            o_phase_c=self.phase_c.status
        )