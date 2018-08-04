'''
encoding: utf-8
author: 
'''

import win32api, win32con, win32gui, win32ui, win32clipboard 
import time

class Mouse:
    def __init__(self, *args, **kwargs):
        '''
        kwargs: 
            pos2
            posx, posy
        '''
        _, _, (self.posx, self.posy) = win32gui.GetCursorInfo()
        self.t = 0.1

        self.update_position(*args, **kwargs)

    def update_position(self, *args, **kwargs):
        if len(args) == 2:
            self.posx, self.posy = args[0], args[1]
        for key in kwargs:
            if key == 'pos2':
                self.posx, self.posy = kwargs[key]
            elif key == 'posx':
                self.posx = kwargs[key]
            elif key == 'posy':
                self.posy = kwargs[key]
            elif key == 't':
                self.t = kwargs[key]
        
    def move(self, *args):
        '''move mouse to (posx, posy) position'''
        if self.posx and self.posy:
            pos2 = (self.posx, self.posy)
        else:
            if len(args) == 2:
                pos2 = (args[0], args[1])
            else:
                print('Wrong args.')
        win32api.SetCursorPos(pos2)

        # update the mouse position
        self.update_position(pos2)

    def right_click(self, *args, **kwargs):
        self.update_position(*args, **kwargs)
        self.move(*args, **kwargs)

        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(self.t)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)     

    def left_click(self, t = 0.1):
        self.update_position(*args, **kwargs)
        self.move(*args, **kwargs)

        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
        time.sleep(t)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)       

    def long_left_click(self, posx_f, posy_f, posx_i, posy_i, t = 2.):
        self.move(posx_i, posy_i)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(t)
        self.move(posx_f, posy_f)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)