from pynput.keyboard import Key, Controller
import time

lol = Controller()

time.sleep(2)
for a in range(0,100):
    lol.press(Key.up)
    lol.release(Key.up)
    time.sleep(1/5)
    with lol.pressed(Key.ctrl):
       lol.press('a')
       lol.release('a')
    lol.press(Key.backspace)
    lol.release(Key.backspace)
    lol.press(Key.enter)
    lol.release(Key.enter)
    time.sleep(1/5)
    lol.press(Key.enter)
    lol.release(Key.enter)
    time.sleep(1/5)
    lol.type('a')
    time.sleep(1/5)
    lol.press(Key.backspace)
    lol.release(Key.backspace)
    time.sleep(1/2)

