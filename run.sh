#!/bin/bash
python aidon_forward.py /dev/ttyUSB0 --influx_host http://<IP>:8086 --influx_db <DATABASE>
