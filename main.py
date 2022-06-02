import app
import threading
import sys

if 'noscan' not in sys.argv:
    import scan
    scan_thread = threading.Thread(target=scan.run, args=(app.send_code,), daemon=True)

if __name__ == '__main__':
    if 'noscan' not in sys.argv:
        scan_thread.start()
    app.run()
