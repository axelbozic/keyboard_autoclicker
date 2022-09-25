from pynput.keyboard import Controller
import keyboard
import sys
from time import sleep

file = open('Data.txt')
Data = file.readlines()
keyboard_ = Controller()
Delay = float(Data[0].split(':', 1)[1])
keyChar = Data[1].split(':', 1)[1]
loopStatus = False


def keypressFcn():
    keyboard_.press(keyChar)
    keyboard_.release(keyChar)


if __name__ == '__main__':
    try:
        while True:
            if not loopStatus:
                if keyboard.is_pressed('*'):
                    loopStatus = True
            elif loopStatus:
                if keyboard.is_pressed('-'):
                    loopStatus = False
            if keyboard.is_pressed('ctrl+x'):
                sys.exit(0)
            if loopStatus:
                keypressFcn()
                sleep(Delay)
    except Exception as e:
        sys.exit(0)
