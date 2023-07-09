import sys
from global_hotkeys import *

is_alive = True


def ctrl_f2():
    print(" You pressed control + F2.")


def ctrl_f3():
    print(" You pressed control + F3.")


def ctrl_f6():
    print(" You pressed control + F4.")


def ctrl_f12():
    global is_alive
    print(" You have pressed control + F12, exiting the program now.")
    is_alive = False
    sys.exit()



bindings = [
    [["control", "f2"], None, ctrl_f2],
    [["control", "f3"], None, ctrl_f31],
    [["control", "f6"], None, ctrl_f6],
    [["control", "f12"], None, ctrl_f12],
]

while is_alive:
    sleep(0.1)
