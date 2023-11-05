#pip install pybluez
import bluetooth

class blebt00:
    def __init__(self):
        self.bt00MACAddress = '98:DA:60:08:32:06'   #bt07 Macadress
        #self.bt00MACAddress = '98:DA:60:07:A1:3A'    #bt08 Macadress
        #self.bt00MACAddress = '98:DA:60:08:1D:D0'    #bt25 Macadress
        self.port = 1   #port 1 is basic port for using ble
        self.socekt = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def bleconnect(self):
        self.socekt.connect((self.bt00MACAddress, self.port))
        return self.socekt
    def bleclose(self):
        self.socket.close()