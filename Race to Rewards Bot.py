from pyautogui import *
import pyautogui
import time
import keyboard
import win32api, win32con

time.sleep(2)
inMiddleLane = True

def left(b):
    if(b):
        win32api.keybd_event(0x25, 0, 0, 0)
        time.sleep(0.05)
        win32api.keybd_event(0x25, 0, win32con.KEYEVENTF_KEYUP, 0)

def right(b):
    if(b == False):
        win32api.keybd_event(0x27, 0, 0, 0)
        time.sleep(0.05)
        win32api.keybd_event(0x27, 0, win32con.KEYEVENTF_KEYUP, 0)

while keyboard.is_pressed('c') == False:

    pic = pyautogui.screenshot(region=(660,130,600,300))  #region of screen for top portion of the road

    width, height = pic.size
    #watch left lane
    for x in range(0,200,2):
        for y in range(0,height,2):

            r,g,b = pic.getpixel((x,y))

            if inMiddleLane == False:
                if r in range(149,152) and g in range(221,226) and b in range(229,235):  #RGB for Blue chemicals
                    right(inMiddleLane)
                    inMiddleLane = True
                    time.sleep(0.4)
                    break
                if r in range(76,80) and g in range(212,218) and b in range(63,69):  #RGB for Green chemicals
                    right(inMiddleLane)
                    inMiddleLane = True
                    time.sleep(0.4)
                    break
                if r in range(233,239) and g in range(238,244) and b in range(167,173):  #RGB for Yellow chemicals
                    right(inMiddleLane)
                    inMiddleLane = True
                    time.sleep(0.4)
                    break

            #check for bonuses in left while in middle
            if inMiddleLane == True:
                if r in range(135,145) and g in range(36,47) and b in range(32,46): #RGB for Guac
                    left(inMiddleLane)
                    inMiddleLane = False
                    time.sleep(0.4)
                    break
                if r in range(25,33) and g in range(24,32) and b in range(22,28): #RGB for Bag and Shoes
                    left(inMiddleLane)
                    inMiddleLane = False
                    time.sleep(0.4)
                    break
    
    #watch middle lane
    for x in range(200,400,2):
        for y in range(0,height,2):

            r,g,b = pic.getpixel((x,y))
            if inMiddleLane == True:
                if r in range(149,152) and g in range(221,226) and b in range(229,235):   #RGB for Blue chemicals
                    left(inMiddleLane)
                    inMiddleLane = False
                    time.sleep(0.4)
                    break
                if r in range(76,80) and g in range(212,218) and b in range(63,69):   #RGB for Green chemicals
                    left(inMiddleLane)
                    inMiddleLane = False
                    time.sleep(0.4)
                    break
                if r in range(233,239) and g in range(238,244) and b in range(167,173):   #RGB for Yellow chemicals
                    left(inMiddleLane)
                    inMiddleLane = False
                    time.sleep(0.4)
                    break

            #while in left, check for bonuses in middle
            if inMiddleLane == False:
                if r in range(135,145) and g in range(36,47) and b in range(32,46):   #RGB for Guac
                    right(inMiddleLane)
                    inMiddleLane = True
                    time.sleep(0.4)
                    break
                if r in range(25,33) and g in range(24,32) and b in range(22,28):   #RGB for Bag and Shoes
                    right(inMiddleLane)
                    inMiddleLane = True
                    time.sleep(0.4)
                    break
