#pip install pybluez
import bluetooth
import time

def bluetoothsetup():
    serverMACAddress = '98:DA:60:07:A1:3A' #목표 주소
    port = 1    #포트는 1번으로 사용하는 것이 일반적
    socekt = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socekt.connect((serverMACAddress, port))
    return socekt

#사용 예시
socket = bluetoothsetup()
while(1):
    socket.send("led 1 on\r\n")
    time.sleep(1)
    socket.send("led 1 off\r\n")
    time.sleep(1)
socket.close()