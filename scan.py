import atexit
from time import sleep

SCANNER_PATH = '/dev/ttyUSB0'

NUL = 0x00
CMD = 0x01
STX = 0x02
ETX = 0x03


def run(callback):
    scanner = open(file=SCANNER_PATH, mode='rb')

    atexit.register(scanner.close)

    while True:
        sleep(0.01)
        line = scanner.readline()
        if line != b'\n':
            callback(line[:-3].decode())

if __name__ == '__main__':
    run(print)
