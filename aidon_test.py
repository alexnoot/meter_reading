#!/usr/bin/python

import serial
import time
import sys
from aidon_obis import *


if len(sys.argv) != 2:
    print "Usage: ... <serial_port>"
    sys.exit(0)


def aidon_callback(fields):
    # print fields
    # Better printout of fields
    if len(fields) == 1:
        print "P in (active)              : " + str(fields["p_act_in"])
        print "----------------------------------------"
    elif len(fields) == 13:
        print "P in / out (active)        : " + str(fields["p_act_in"]) + " / " + str(fields["p_act_out"])
        print "P in / out (reactive)      : " + str(fields["p_react_in"]) + " / " + str(fields["p_react_out"])
        print "Voltage / Current (1)      : " + str(fields["ul1"]) + " / " + str(fields["il1"])
        print "Voltage / Current (2)      : " + str(fields["ul2"]) + " / " + str(fields["il2"])
        print "Voltage / Current (3)      : " + str(fields["ul3"]) + " / " + str(fields["il3"])
        print "Meter ID                   : " + str(fields['meter_id']) + " / Type: " + str(fields['meter_type']) + " / Version: " + str(fields['version_id'])
        print "----------------------------------------"
    elif len(fields) == 18:
        print "P in / out (active)        : " + str(fields["p_act_in"]) + " / " + str(fields["p_act_out"])
        print "P in / out (reactive)      : " + str(fields["p_react_in"]) + " / " + str(fields["p_react_out"])
        print "Voltage / Current (1)      : " + str(fields["ul1"]) + " / " + str(fields["il1"])
        print "Voltage / Current (2)      : " + str(fields["ul2"]) + " / " + str(fields["il2"])
        print "Voltage / Current (3)      : " + str(fields["ul3"]) + " / " + str(fields["il3"])
        print "Meter ID                   : " + str(fields['meter_id']) + " / Type: " + str(fields['meter_type']) + " / Version: " + str(fields['version_id'])
        print "Energy in / out (active)   : " + str(fields['energy_act_in']) + " / " + str(fields['energy_act_out'])
        print "Energy in / out (reactive) : " + str(fields['energy_react_in']) + " / " + str(fields['energy_react_out'])
        print "----------------------------------------"
    else:
        print "Error: field length is not 1, 13 or 18"


ser = serial.Serial(sys.argv[1], 2400, timeout=0.05, parity=serial.PARITY_NONE)
a = aidon(aidon_callback)

while (1):
    while ser.inWaiting():
        # DEBUG
        # print ser.inWaiting()
        # HEX PRINT
        # data = ser.read().encode('hex')
        # print data,
        # HEX PRINT END
        a.decode(ser.read(1))

    time.sleep(0.01)
