# Aidon 6534 AMS data parser

This code is updated to work with my Aidon 6534 (400v 3ph) meter (not from Hafslund, but they should be equal).<br>
Please refer to the original [code](https://github.com/skagmo/meter_reading) for more info.

### aidon_obis.py
A class for decoding HDLC and extracting OBIS fields. Requires python module crcmod (sudo pip install crcmod).
*NB: This is not a full COSEM parser, as the number of OBIS fields and their sequence is assumed to be as on a Hafslund meter.*

### aidon_test.py
Test output. This file has been altered for a more readable output. <br/>
```
./aidon_test.py <port>
./aidon_test.py /dev/ttyUSB0
```

### aidon_forward.py
Forward to influxdb and Home Assistant.
Forwarding to only one of them is possible. Just omit the influx* or hass* arguments.
<br/>
Will generate sensors in Home assistant named `sensor.aidon_*`. Not done with a component, so these sensors will disappear on Home Assistant restart, and can't be renamed.
<br/>
For InfluxDB, readings are placed in the provided database under `voltage`, `current`, `power` and `energy`, and key `dev` holds device name (which begins with aidon).

```
python aidon_forward.py \
/dev/ttyUSB0 \
--influx_host http://localhost:8086 \
--influx_db metering \
--hass_host https://myhass.com:8123 \
--hass_token abcdefgh0123456789
```
