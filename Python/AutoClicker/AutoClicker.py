# Alex Miller
# Auto clicker for mouse

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

print()
Keyboard = Controller()
delay = 0.5 # how often it will click, in seconds
button = Button.left # what button to click
start_stop_key = KeyCode(char='=') # start / stop key
print('Start / stop with ' + str(start_stop_key))
stop_key = KeyCode(char='-') # stop the whole program key
print('End program with ' + str(stop_key))

class ClickMouse(threading.Thread): # clicking the mouse
    def __init__(self, delay, button): # constructor
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self): # start clicking-
        self.running = True
        print('Clicker Started')
        print()
    
    def stop_clicking(self): # stop clicking
        self.running = False
        print('Clicker Stopped')
        print()
    
    def exit(self): # exit the program
        self.stop_clicking()
        self.program_running = False
    
    def run(self): # while running
        while self.program_running:
            while self.running:
                Keyboard.press(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)

click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key): # what happens when you press a key
    if key == start_stop_key: # if its the start stop key
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == stop_key: # if its the stop key
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener: # key listener
    listener.join()