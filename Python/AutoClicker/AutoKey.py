import sys
import time
from pynput.keyboard import Listener, KeyCode, Controller, Key

start_stop_key = KeyCode(char='`')
stop_key = KeyCode(char='=')
Keyboard = Controller()
print('Start / Stop key = ' + str(start_stop_key))
print('Stop key = ' + str(stop_key))
running = False
def Run(running):
    while ProgramRunning:
        while running:
            Keyboard.press('Q')
            time.sleep(.001)
        time.sleep(.1)

def on_press(key):
    global running
    if key == start_stop_key:
        if running:
            running = False
            print()
            print('Stopped running')
            print()
            Run(running)
        else:
            running = True
            print()
            print('Started running')
            print()
            Run(running)
    elif key == stop_key:
        listener.stop()
        sys.exit()

with Listener(on_press=on_press) as listener:
    listener.join()
