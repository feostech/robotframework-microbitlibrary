import serial
import uflash

ANALOG_VAL_MAX = 1024
DIGITAL_VAL_MAX = 2

class MicrobitGPIO:

    def __init__(self):
        self.pin = ["pin0", "pin1", "pin2"]

    def connect(self, device, baudrate):
        self.ser = serial.Serial(device, baudrate)

    def runtime_flash(self):
        uflash.flash()

    def write_analog(self, pin, val):
        pin = int(pin)
        val = int(val)
        try:
            if val not in range(ANALOG_VAL_MAX):
                raise ValueError
            cmd = self.pin[pin] + ".write_analog(" + str(val) +")\r\n"
            self.ser.write(cmd.encode("utf-8"))
        except IndexError as err:
            print("Invalid Pin number: should be 0,1,2: ", err)
        except ValueError as err:
            print("Invalid Analog value: should be in range 0 to 1023: ", err)

    def write_digital(self, pin, val):
        pin = int(pin)
        val = int(val)
        try:
            if val not in range(DIGITAL_VAL_MAX):
                raise ValueError
            cmd = self.pin[pin] + ".write_digital(" + str(val) +")\r\n"
            self.ser.write(cmd.encode("utf-8"))
        except IndexError as err:
            print("Invalid Pin number: should be 0,1,2: ", err)
        except ValueError as err:
            print("Invalid Digital value: should be either 0 or 1: ", err)

    def set_analog_period(self, pin, period):
        pin = int(pin)
        period = int(period)
        try:
            if period < 150 or period > 25000:
                raise ValueError("Invalid period value: should be between 150us to 25ms")
            cmd = self.pin[pin] + ".set_analog_period(" + str(period) + ")\r\n"
            self.ser.write(cmd.encode("utf-8"))
        except IndexError as err:
            print("Invalid Pin number: should be 0, 1, or 2:", err)
        except ValueError as err:
            print(err)
