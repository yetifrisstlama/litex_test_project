"""\
 Spartan6 ISERDES receiver for LVDS ADCs

 Needs a DDR clock signal, in phase with the data lanes,
 doing one transition for every bit

 This is basically a migen mash up of
 * serdes_1_to_n_clk_ddr_s8_diff.v
 * serdes_1_to_n_data_ddr_s8_diff.v
 * litevideo/datacapture.py

 Untested so far

 try `python3 IserdesSp6_pll.py build`
 """

from sys import argv
from migen import *
from migen.genlib.cdc import AsyncResetSynchronizer
from IserdesSp6_common import IserdesSp6_common, genVerilog


class IserdesSp6_ddr(IserdesSp6_common):
    def __init__(
        self, S=8, D=2, MIRROR_BITS=False, CLK_EDGE_ALIGNED=True, **kwargs
    ):
        """
        S = serialization factor (bits per frame)
        D = number of parallel lanes

        MIRROR_BITS = False
            first bit of the serial stream clocked in ends up in the
            LSB of data_outs

        CLK_EDGE_ALIGNED = True
            Clock and data lanes are in-phase

        CLK_EDGE_ALIGNED = False
            Clock is 90 deg shifted to data
            (clock transitions in middle of data-eye)

        See IserdesSp6_common.py for input output ports
        """

        ###

        # Add data lanes and control signals
        IserdesSp6_common.__init__(
            self, S, D, MIRROR_BITS,
            {"p_DATA_RATE": "DDR"},
            {"p_DATA_RATE": "DDR"}
        )

        self.specials += AsyncResetSynchronizer(self.sample, self.reset)

        # -------------------------------------
        #  Iserdes DDR clocking scheme
        # -------------------------------------
        dcoo_p = Signal()
        dcoo_n = Signal()
        self.specials += Instance(
            "IBUFDS_DIFF_OUT",
            i_I=self.dco_p,
            i_IB=self.dco_n,
            o_O=dcoo_p,
            o_OB=dcoo_n
        )
        dco_del_p = Signal()
        dco_del_n = Signal()
        # Add 90 degree phase shift to clock if it is not edge aligned
        self.idelay_default["p_IDELAY_TYPE"] = \
            "FIXED" if CLK_EDGE_ALIGNED else "VARIABLE_FROM_HALF_MAX"
        self.specials += Instance(
            "IODELAY2",
            p_SERDES_MODE="MASTER",
            i_IDATAIN=dcoo_p,
            i_CAL=self.idelay_cal_m,
            o_DATAOUT=dco_del_p,
            **self.idelay_default
        )
        self.specials += Instance(
            "IODELAY2",
            p_SERDES_MODE="SLAVE",
            i_IDATAIN=dcoo_n,
            i_CAL=self.idelay_cal_s,
            o_DATAOUT=dco_del_n,
            **self.idelay_default
        )
        divclk = Signal()
        self.specials += Instance(
            "BUFIO2_2CLK",
            p_DIVIDE=S,
            i_I=dco_del_p,
            i_IB=dco_del_n,
            o_IOCLK=self.ioclk_p,
            o_DIVCLK=divclk,
            o_SERDESSTROBE=self.serdesstrobe
        )
        self.specials += Instance(
            "BUFG",
            i_I=divclk,
            o_O=ClockSignal("sample")
        )
        self.specials += Instance(
            "BUFIO2",
            p_I_INVERT="FALSE",
            p_DIVIDE_BYPASS="FALSE",
            p_USE_DOUBLER="FALSE",
            i_I=dco_del_n,
            o_IOCLK=self.ioclk_n
        )


if __name__ == "__main__":
    if "build" not in argv:
        print(__doc__)
        exit(-1)
    genVerilog(IserdesSp6_ddr)
