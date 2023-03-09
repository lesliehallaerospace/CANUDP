import os
import can
import socket

# Configure CAN connection
os.system('sudo ip link set can0 type can bitrate 500000')
os.system('sudo ifconfig can0 up')
can0 = can.interface.Bus(channel='can0', bustype='socketcan')  # socketcan_native

# Configure UDP Connection
UDP_IP = "169.254.212.136"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

# Configure BLF Writer
write = can.BLFWriter(sock)

try:
    while True:
        msg = can0.recv(1)
        if msg is not None:
            print(msg)
            write.on_message_received(msg)
            sock.sendto(write, (UDP_IP, UDP_PORT))

except KeyboardInterrupt:
    write.stop()
    os.system('sudo ifconfig can0 down')
    pass
