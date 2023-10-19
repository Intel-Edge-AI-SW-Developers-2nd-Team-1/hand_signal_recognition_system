#pip install pybluez
import bluetooth
import time

def bluetoothsetup():
    serverMACAddress = '98:DA:60:07:A1:3A' #��ǥ �ּ�
    port = 1    #��Ʈ�� 1������ ����ϴ� ���� �Ϲ���
    socekt = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socekt.connect((serverMACAddress, port))
    return socekt

#��� ����
socket = bluetoothsetup()
while(1):
    socket.send("led 1 on\r\n")
    time.sleep(1)
    socket.send("led 1 off\r\n")
    time.sleep(1)
socket.close()