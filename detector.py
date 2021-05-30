from pynput.keyboard import *

def press_on(key):
    print('Press ON: {}'.format(key))

def press_of(key):
    print('Press OFF: {}'.format(key))
    if key == Key.esc:
        return False
        
with Listener(on_press = press_on, on_release = press_off) as listener:
    listener.join()
