import time
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ble.ble_module import blebt00
import cv2

bt = blebt00()
bt07socekt = bt.bleconnect()
while (1):
    bt07socekt.send("order 0\r\n")
    # bt07socekt.send("go\r\n")
    time.sleep(3)
    bt07socekt.send("order 1\r\n")
    # bt07socekt.send("go\r\n")
    time.sleep(3)
    bt07socekt.send("order 2\r\n")
    # bt07socekt.send("stop\r\n")
    time.sleep(3)
    bt07socekt.send("order 3\r\n")
    # bt07socekt.send("left\r\n")
    time.sleep(3)
    bt07socekt.send("order 4\r\n")
    # bt07socekt.send("right\r\n")
    time.sleep(3)
    bt07socekt.send("order 6\r\n")
    # bt07socekt.send("right\r\n")
    time.sleep(3)
    '''
    key = cv2.waitKey(100) & 0xFF
    if key == ord('q'):
        bt07socekt.send("order 0\r\n")
        break
    elif key == ord('w'):
        bt07socekt.send("order 4\r\n")
    elif key == ord('a'):
        bt07socekt.send("order 2\r\n")
    elif key == ord('s'):
        bt07socekt.send("order 6\r\n")
    elif key == ord('d'):
        bt07socekt.send("order 3\r\n")
    elif key == ord('e'):
        bt07socekt.send("order 0\r\n")
    '''
bt.bleclose()

'''
#use example
def bluetoothsetup():
    bt00MACAddress = '98:DA:60:08:32:06'    #bt07 Macadress
    #bt00MACAddress = '98:DA:60:07:A1:3A'    #bt08 Macadress
    #bt00MACAddress = '98:DA:60:08:1D:D0'    #bt25 Macadress

    port = 1    #port 1 is basic port for using ble
    socekt = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socekt.connect((bt00MACAddress, port))
    return socekt

socket = bluetoothsetup()
while(1):
    socket.send("order 1\r\n")
    time.sleep(1)
    socket.send("order 2\r\n")
    time.sleep(1)
socket.close()
'''