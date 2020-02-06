import app, scan
import threading

app_thread = threading.Thread(target=app.run, daemon=True)


def print_code(barcode):
    print(barcode)


if __name__ == '__main__':
    app_thread.start()
    scan.run(print_code)
