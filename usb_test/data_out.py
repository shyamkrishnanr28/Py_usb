""" This test initiates EP1 OUT transfer, then prints the tx data length """
import usb.core
import usb.util

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

# write the data
# tx_length = dev.write(0x01, "Test data tx", 100)
tx_length = ep_out.write("Test data tx")

print "tx_length is", tx_length
