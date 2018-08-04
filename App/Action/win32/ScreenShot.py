'''
encoding: utf-8
author: 

https://www.programcreek.com/python/example/62809/win32ui.CreateBitmap
https://stackoverflow.com/questions/41785831/how-to-optimize-conversion-from-pycbitmap-to-opencv-image
'''

import os
import copy
import numpy as np
import win32api, win32con, win32gui, win32ui, win32clipboard 
from PIL import Image

class ScreenShot:
    def __init__(self, *args, **kwargs):
        '''
        kwargs: 
            path: stored screenshot
        '''
        # initialize
        self.pos2_monitor = (win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1))
        self.pos4 = [0, 0, self.pos2_monitor[0], self.pos2_monitor[1]]
        self.path = None

        self.set_parameters(*args, **kwargs)
        self.pre_get_bitmap(*args, **kwargs)

    def set_parameters(self, *args, **kwargs):
        for key in kwargs:
            if key == 'path':
                self.path = kwargs[key]
            elif key == 'pos4':
                self.pos4 = kwargs[key]

    def pre_get_bitmap(self, *args, **kwargs):
        pos4 = self.pos4
        self.hwnd = 0
        self.size = tuple(map(lambda x, y: x - y, pos4[2:4], pos4[0:2]))

        self.wDC = win32gui.GetWindowDC(self.hwnd)
        self.dcObj = win32ui.CreateDCFromHandle(self.wDC)
        self.cDC = self.dcObj.CreateCompatibleDC()
        self.data_bitmap = win32ui.CreateBitmap()
        self.data_bitmap.CreateCompatibleBitmap(self.dcObj, self.size[0], self.size[1])
        self.cDC.SelectObject(self.data_bitmap)   
        self.cDC.BitBlt((0,0), self.size, self.dcObj, self.pos4[0:2], win32con.SRCCOPY)

    def free_space(self):
        # Free Resources
        self.dcObj.DeleteDC()
        self.cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, self.wDC)
        win32gui.DeleteObject(self.data_bitmap.GetHandle()) 

    def save(self, *args, **kwargs):
        if not self.path:
            path_screenshot = os.path.join(os.getcwd(), 'temp.bmp')
        else:
            path_screenshot = self.path

        self.data_bitmap.SaveBitmapFile(cDC, path_screenshot)
        self.free_space()

    def get_string(self, *args, **kwargs):
        signedIntsArray = self.data_bitmap.GetBitmapBits(True)
        self.free_space()
        return signedIntsArray
    
    def get_numpy_1d(self):
        img_1d_np_array = np.fromstring(self.get_string(), dtype='uint8')
        return img_1d_np_array

    def get_numpy_shaped(self):
        img_np_shaped = self.get_numpy_1d().reshape(self.size[1], self.size[0], 4)
        return img_np_shaped

    def get_img(self):
        img = Image.fromarray(self.get_numpy_shaped(), 'RGBA')
        return img