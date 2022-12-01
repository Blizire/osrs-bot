import pyautogui
from scanner import find
import os
import time
import random

cur_path = os.getcwd()

goblin_pixels = [(26,75,42), (26,75,42), (29,82,46), (25,72,41)]
goblin_pixel = (133,140,35)
attack_button = "\\imgs\\option_attack.png"
monster = {
    "goblin":(133,140,35)
}

def autoFight(npc):
    try:
        while True:
            pixel = monster[npc]
            pos = find.startPixelScan(pixel, 100, 130, 525, 330)
            if pos != None:
                x, y = pos[0]
                pyautogui.moveTo(x, y)
                pyautogui.click(button="right")
                btn_cords = pyautogui.locateCenterOnScreen(cur_path + attack_button)
                bx = None
                by = None
                if(btn_cords != None):
                    bx, by = btn_cords
                if bx != None and by != None:
                    pyautogui.moveTo(bx, by)
                    time.sleep(0.5)
                    pyautogui.click(button="left")
                    time.sleep(random.randint(10, 15))
            else:
                pass
    except KeyboardInterrupt as e:
        print("Stopping autocombat")
        return None
