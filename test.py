import app, scan
import threading

app_thread = threading.Thread(target=app.run, daemon=True)


if __name__ == '__main__':
    app_thread.start()
    while True:
        code = input('Enter barcode or noting to exit: ')
        if code == '':
            break
        app.send_code(code)