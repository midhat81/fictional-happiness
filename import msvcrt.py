import msvcrt
from time import sleep
def a():
    for n in range(10):
        if msvcrt.kbhit():
            return msvcrt.getch()
        sleep(1)