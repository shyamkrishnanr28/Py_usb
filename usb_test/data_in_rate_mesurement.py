import usb.core
import usb.util
import time
import math

# Rx Data length in bytes, should be a multiple of 512
# RX_DATA_LENGTH = 512 * 32 # For USB 3.0
RX_DATA_LENGTH = 512 * 2 # For USB 2.0

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

ep_in = usb.util.find_descriptor(
    intf,
    # match the first IN endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_IN)

assert ep_in is not None

print "\n", ep_in, "\n"

cnt = 0
time1 = time.time()
time2 = 0

# Read the data
while True:
    # Discard the rx data
    ep_in.read(RX_DATA_LENGTH, 5000)
    cnt = cnt + 1

    time2 = time.time()
    if time2 > (time1 + 1):
        time1 = time2
        print float((cnt * RX_DATA_LENGTH)/1000), "KBPS"
        cnt = 0
