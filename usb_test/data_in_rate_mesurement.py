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
    read_data = ep_in.read(512, 5000)
    cnt = cnt + 1

    time2 = time.time()

    if time2 > (time1 + 1):
        time1 = time2
        print float((cnt * 512)/1000), "KBPS"
        cnt = 0
