"""
Hello world example for the ZedBoard with litex
"""
import sys
from migen import *
from litex.boards.platforms import zedboard

p = zedboard.Platform()

def main():
    led = p.request("user_led")
    module = Module()
    # 100e6 Hz / 2**26 = 1.49 Hz
    counter = Signal(26)
    module.comb += led.eq(counter[25])
    module.sync += counter.eq(counter + 1)
    p.build(module)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "prog":
        prog = p.create_programmer("openocd")
        prog.load_bitstream("build/top.bit")
    else:
        main()

