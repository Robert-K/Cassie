import app
import threading
from time import sleep


def test_function():
    while True:
        print('Test thread running...')
        sleep(5)


test_thread = threading.Thread(target=test_function, daemon=True)

if __name__ == '__main__':
    test_thread.start()
    print('Test thread started.')
    app.run()
