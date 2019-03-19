from pynput import mouse
from pynput.mouse import Button, Controller
#import tkinter
class MyException(Exception): pass
#Get Screen Info
#root = tkinter.Tk()
#SCREEN_WIDTH = root.winfo_screenwidth()
#SCREEN_HEIGHT = root.winfo_screenheight()

class Mouse:
#    def __init__(self):
#        mouseX = SCREEN_WIDTH/2
#        mouseY = SCREEN_HEIGHT/2
#        mouse = Controller()
#        mouse.position = (mouseX, mouseY)

    def on_move(self, x, y):
        print('Pointer moved to {0}'.format((x, y)))
        self.x = x
        self.y = y
#        print(mouseX)

    def on_click(self, x, y, button, pressed):
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        if not pressed:
            # Stop listener
            return False

    with mouse.Listener(
        on_move=on_move,
        on_click=on_click) as listener:
        listener.join()     