from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGEventLeftMouseDragged
from Quartz.CoreGraphics import kCGHIDEventTap
from Quartz.CoreGraphics import kCGEventRightMouseDown
from Quartz.CoreGraphics import kCGEventRightMouseUp
import Quartz as Qz

import time

def mouseEvent(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(
                None,
                type,
                (posx, posy),
                kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
    mouseEvent(kCGEventMouseMoved, posx, posy);

def mouseclick(posx,posy):
    # uncomment this line if you want to force the mouse
    # to MOVE to the click location first (I found it was not necessary).
    #mouseEvent(kCGEventMouseMoved, posx,posy);
    mouseEvent(kCGEventLeftMouseDown, posx, posy);
    time.sleep(0.1)
    mouseEvent(kCGEventLeftMouseUp, posx, posy);

def mouse_drag(posxs, posys, posxd, posyd):
    # set focus on location before begin dragging
    mouseclick(posxs, posys)
    time.sleep(0.5)
    #dragging sequence
    mouseEvent(kCGEventLeftMouseDown, posxs, posys)
    mouseEvent(kCGEventLeftMouseDragged, posxd, posyd)
    mouseEvent(kCGEventLeftMouseUp, posxd, posyd)

def right_click(posx, posy):
    mouseEvent(kCGEventRightMouseDown, posx, posy)
    mouseEvent(kCGEventRightMouseUp, posx, posy)

def long_click(posx, posy, how_long):
    mouseEvent(kCGEventLeftMouseDown, posx, posy)
    time.sleep(how_long)
    mouseEvent(kCGEventLeftMouseUp, posx, posy)
#
# def get_mouse_clicked_location():
#     px, py = Qz.CGEventGetLocation(kCGEventLeftMouseDown)
#     print px, py
#     return px, py
