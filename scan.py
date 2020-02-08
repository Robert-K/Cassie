import atexit
from time import sleep
import serial

SCANNER_PATH = '/dev/ttyUSB0'
BAUD = 115200

NUL = 0x00
CMD = 0x01
STX = 0x02
ETX = 0x03


def run(callback):
    ser = serial.Serial(SCANNER_PATH, BAUD, timeout=0)

    atexit.register(ser.close)

    while True:
        print("test")
        line = ser.readline()
        if line != b'\n':
            callback(line[:-3].decode())


if __name__ == '__main__':
    run(print)
