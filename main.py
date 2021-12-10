import os
import platform
import time
from datetime import datetime


def ping():
    param = '-n' if platform.system() == 'Windows' else '-c'
    hostname = "google.com"
    response = os.system(f"ping {param} 1 " + hostname)

    return response


def logs():
    current_time = datetime.now().strftime("%H:%M:%S")
    f = open("logs.txt", "a")
    f.write(f"{current_time} : Internet was down\n")
    f.close()


def main(delay):
    with open("logs.txt", 'w') as f:
        f.close()

    while True:
        if ping() != 0:
            logs()
        time.sleep(delay)


if __name__ == '__main__':
    main(60)

