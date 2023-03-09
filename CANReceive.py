import os
import can

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')

msg = can0.recv(20)
print (msg)
if msg is None:
    print('Timeout occured, no message.')

os.system('sudo ifconfig can0 down')