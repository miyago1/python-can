"""
Script to run from transmitting Beaglebone to send secure CAN messages.
"""


import can
import time
from can.protocols.secure.securemessage import SecureMessage
from can.protocols.secure.arbitrationid import ArbitrationID
from can.protocols.secure import Bus

interface = 'vcan0'

NO_OF_MSGS = 99

bus = Bus(channel=interface, claimed_addresses=[0, 1])
arb = ArbitrationID(priority=5, destination_addresses = [1], source_address=bus.local_node.address)
sum = 0
for i in range(NO_OF_MSGS, 0, -1):
    start_time = time.time()
    msg = SecureMessage(data=[i], arbitration_id=arb)
    bus.send(msg)
    timer = time.time() - start_time
    sum += timer


print "average sending time per msg: ", sum/NO_OF_MSGS
