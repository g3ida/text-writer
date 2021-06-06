import pynput
import random

from pynput.keyboard import Key, Controller
import pyperclip
import time

KeyComb_Quit = [
    {pynput.keyboard.Key.ctrl_r}
]

current = set()
keyboard = Controller()

def on_press(key):
    if any([key in comb for comb in KeyComb_Quit]):
        current.add(key)
        print(current)
        if any(all(k in current for k in comb) for comb in KeyComb_Quit):
            #print("hola")
            pasteCode()


def on_release(key):
    try:
        current.remove(key)
    except KeyError:
        pass


def pasteCode():
    time.sleep(1)
    s = pyperclip.paste()
    for key in s :
        keyboard.press(key)
        keyboard.release(key)
        time.sleep((random.randint(0, 9) / 100.0) + 0.07)


listener = pynput.keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

##### MAIN Script #####
while True:
    time.sleep(0.01)