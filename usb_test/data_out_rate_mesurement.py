""" This test initiates EP1 OUT transfer, then prints the tx data length """
import usb.core
import usb.util
import time
import math

# find our device
dev = usb.core.find(idVendor=0x04b4, idProduct=0x00f1)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep_out = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep_out is not None

print "\n", ep_out, "\n"

cnt = 0
time1 = time.time()
time2 = 0
tx_data = []

for x in range(512):
    # Appended value shall be <= 0xff
    tx_data.append(0xAA)

# write the data
while True:
    ep_out.write(tx_data)
    cnt = cnt + 1

    time2 = time.time()

    if time2 > (time1 + 1):
        time1 = time2
        print float((cnt * 512)/1000), "KBPS"
        cnt = 0
