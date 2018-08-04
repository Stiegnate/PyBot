'''
encoding: utf-8
author: jibancat

most of the scripts are adopted from 
GeekOrgy.com 
http://web.archive.org/web/20111229234504/http://www.geekorgy.com:80/index.php/2010/06/python-mouse-click-and-move-mouse-in-apple-mac-osx-snow-leopard-10-6-x/
'''
import sys
import time
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved 
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap

class MouseAction:

    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy

    def update_position(self, posx, posy):
        self.posx = posx
        self.posy = posy        

    def mouseEvent(self, type, posx, posy):
        '''create a mouse event and post'''
        theEvent = CGEventCreateMouseEvent(None, type, (posx, posy), kCGMouseButtonLeft)
        CGEventPost(kCGHIDEventTap, theEvent)

    def mouseMove(self, posx, posy):
        '''move mouse to (posx, posy) position'''
        self.mouseEvent(kCGEventMouseMoved, posx, posy)

        # update the mouse position
        self.update_position(posx, posy)

    def mouseClick(self):
        '''click the mouse'''
        self.mouseEvent(kCGEventLeftMouseDown, self.posx, self.posy)
        self.mouseEvent(kCGEventLeftMouseUp,   self.posx, self.posy)

    def mouseClickDown(self):
        self.mouseEvent(kCGEventLeftMouseDown, self.posx, self.posy)

    def mouseClickUp(self):
        self.mouseEvent(kCGEventLeftMouseUp,   self.posx, self.posy)        