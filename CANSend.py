import os
import can

os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan')

msg = can.Message(arbitration_id = 0x12, data = [0,1,2,3,4,5,6,7], is_extended_id = False)
can0.seng.msg

os.system('sudo ifconfig can0 down')