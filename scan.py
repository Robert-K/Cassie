PORT = "/dev/ttyUSB0"


def run(callback):
    dev = open(PORT, "r")
    barcode = ""
    try:
        while True:
            byte = dev.read(1)
            if byte == "\xA6":
                dev.read(3)
                callback(barcode)
                barcode = ""
            else:
                barcode += byte
    finally:
        dev.close()
