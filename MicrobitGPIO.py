import serial
import uflash

ANALOG_VAL_MAX = 1023

class MicrobitGPIO:

    def __init__(self):
        self.pin = ["pin0", "pin1", "pin2"]

    def connect(self, device, baudrate):
        self.ser = serial.Serial(device, baudrate)

    def runtime_flash(self):
        uflash.flash()

    def write_analog(self, pin, val):
        try:
            if val not in range(ANALOG_VAL_MAX):
                raise ValueError
            cmd = self.pin[pin] + ".write_analog(" + str(val) +")\r\n"
            self.ser.write(cmd.encode("utf-8"))
        except IndexError as err:
            print("Invalid Pin number: should be 0,1,2: ", err)
        except ValueError as err:
            print("Invalid Analog value: should be in range 0 to 1023: ", err)
