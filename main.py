import app
import scan
import threading

scan_thread = threading.Thread(target=scan.run, args=(app.send_code,), daemon=True)

if __name__ == '__main__':
    scan_thread.start()
    app.run()
