#!/bin/bash
# Remotely starts up the litex server with shared memory access,
# then it tunnels the etherbone port 1234 over ssh
HOSTNAME=spaetzle.dhcp
ssh -L 1234:localhost:1234 $HOSTNAME "cd litex_server; sudo python3 litex_server.py --devmem --devmem-offset 0x43c00000"
