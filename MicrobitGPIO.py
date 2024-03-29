import serial
import uflash

class MicrobitGPIO:
   
    def mbit_connect(self, device, baudrate):
        self.ser = serial.Serial(device, baudrate)

    def mbit_runtime_flash(self):
        uflash.flash()

    def write_analog(self, val):
        cmd = "pin1.write_analog(" + str(val) +")\r\n"
        self.ser.write(cmd.encode("utf-8"))

