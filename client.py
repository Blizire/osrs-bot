import win32gui
import pyautogui
import time
from datetime import datetime
from rs_data import item
from rs_data import monster
from osrs_buttons import inventory
from osrs_buttons import buttons
from osrs_buttons import windows
from mouse_nfo import mouse_nfo
from scanner import find
from fighter import fight

def help():
    print("""[help menu]
    COMMANDS:\n
    setup     : resetup windows for cosole and game
    login     : login into game client (must be at start screen)
    logout    : log out of game (must be logged in)
    bone      : buries all regular bones
    reset     : resets in game view
    help      : shows this screen
    """)

def setWindowHandle(name):
    hwnd = win32gui.FindWindow(None, name)
    return hwnd

def setupWindow(hwnd, wdow_xpos, wdow_ypos, wdow_width, wdow_height):
    if not hwnd:
        print("[error] setupWindow hwnd was None")
    win32gui.MoveWindow(hwnd, wdow_xpos, wdow_ypos, wdow_width, wdow_height, True)

def selectWindow(hwnd, x, y):
    if not hwnd:
        print("[error] selectWindow hwnd was None")
    win32gui.SetForegroundWindow(hwnd)
    pyautogui.click(x=x, y=y, button="left")

def login(username, password):
    xpos_login = 567
    ypos_login = 420
    xpos_click_to_play = 498
    ypos_click_to_play = 462
    pyautogui.keyDown("enter")
    pyautogui.typewrite(username)
    pyautogui.keyDown("tab")
    time.sleep(1)
    pyautogui.typewrite(password)
    pyautogui.keyDown("enter")
    pyautogui.moveTo(100, 100)
    for i in range(5):
        print("[login] loading..")
        time.sleep(1)
        img = pyautogui.locateCenterOnScreen("imgs/clicktoplay.png",
                                            grayscale=True,
                                            region=(100,100,800,600))
        if(img):
            break
    if(img):
        pyautogui.click(x=xpos_click_to_play,
                        y=ypos_click_to_play,
                        clicks=1,
                        button="left")
        print("[log in complete]")
    else:
        print("[warning] couldn't click to play")

def resetView():
    xpos_compass = 678
    ypos_compass = 150
    pyautogui.click(x=xpos_compass,
                    y=ypos_compass,
                    clicks=1,
                    button="left")
    for i in range(5):
        pyautogui.keyDown('up')
    x, y = buttons.window_poi["osrs_settings_icon"]
    pyautogui.click(x, y)
    x, y = buttons.window_poi["osrs_settings_display_icon"]
    pyautogui.click(x, y)
    x, y = buttons.window_poi["osrs_settings_display_min_zoom"]
    pyautogui.click(x, y)
    x, y = buttons.window_poi["osrs_inventory"]
    pyautogui.click(x, y)



def logOut():
    xpos_menu_icon = 758
    ypos_menu_icon = 614
    pyautogui.click(x=xpos_menu_icon, y=ypos_menu_icon, button="left")
    time.sleep(1)
    xpos_logout_btn = 760
    ypos_logout_btn = 550
    pyautogui.click(x=xpos_logout_btn, y=ypos_logout_btn, button="left")
    print("[logged out]")

def getConfNfo(typenfo, path):
    fp_config = open(path,'r')
    config = fp_config.readlines()
    for i in config:
        key = i.split(":")[0]
        val = i.split(":")[1]
        if(key == typenfo):
            return val.rstrip("\n\r")
    print("[error] unknown config type: %s" % typenfo)
    fp_config.close()
    quit()

def autofight(npc):
    x, y = windows.wdow_info["osrs_main_display_x1_y1"]
    x2, y2 = windows.wdow_info["osrs_main_display_x2_y2"]
    width = abs(x - x2)
    height = abs(y - y2)
    for monster_block in monster.monster_path[npc]:
        results = find.startScan(monster_block, x, y, width, height)
        print(results)


def main():
    shell_name = getConfNfo("shellname", "config.txt")
    username = getConfNfo("username", "config.txt")
    password = getConfNfo("password", "config.txt")
    #window constants
    wdow_xpos = 100
    wdow_ypos = 100
    wdow_width = 800
    wdow_height = 600
    wdow_console_xpos = wdow_xpos + wdow_width
    wdow_osrs_name = "Old School RuneScape"          #  these names represent the window
    wdow_console_name = win32gui.GetWindowText(win32gui.GetForegroundWindow()) # names that the script hooks onto
    #in game window constants
    osrs_inventory_origin_pos_x, osrs_inventory_origin_pos_y = 662,334
    osrs_inventory_width = 190
    osrs_inventory_height = 264
    hwnd = setWindowHandle(wdow_osrs_name)
    if not hwnd:
        print("[error] couldn't grab game window")
    else:
        setupWindow(hwnd,
                wdow_xpos,
                wdow_ypos,
                wdow_width,
                wdow_height)
        selectWindow(hwnd, wdow_xpos, wdow_ypos)

    hwnd_console = setWindowHandle(wdow_console_name)
    if not hwnd_console:
        print("[error] couldn't grab console window")
    else:
        setupWindow(hwnd_console,
                wdow_console_xpos,
                        wdow_ypos,
                        wdow_width,
                        wdow_height)
        selectWindow(hwnd, wdow_console_xpos, wdow_ypos)

    # command console
    while(True):
        if not hwnd:
            print("[error] console caught None in game handle")
        if not hwnd_console:
            print("[error] console caught None in console handle")
        print()
        cmd = input("%s $ " % shell_name)
        selectWindow(hwnd, wdow_xpos, wdow_ypos)
        if(cmd == "setup"):
            setupWindow(hwnd,
                    wdow_xpos,
                    wdow_ypos,
                    wdow_width,
                    wdow_height)
            setupWindow(hwnd_console,
                            wdow_console_xpos,
                            wdow_ypos,
                            wdow_width,
                            wdow_height)
        elif(cmd == "login"):
            login(username, password)
        elif(cmd == "logout"):
            logOut()
        elif(cmd == "reset"):
            resetView()
        elif(cmd == "quickDrop"):
            selectWindow(hwnd_console, wdow_console_xpos, wdow_ypos)
            item_name = input("item to drop: ")
            inventory.quickDrop(item_name)
        elif(cmd == "fight"):
            selectWindow(hwnd_console, wdow_console_xpos, wdow_ypos)
            monster = input("npc to hunt: ")
            fight.autoFight(monster)
        elif(cmd == "bone"):
            inventory.quickBury()
        elif(cmd == "mouse"):
            try:
                selectWindow(hwnd_console, wdow_console_xpos, wdow_ypos)
                mouse_nfo.start()
            except KeyboardInterrupt:
                print("[mouse] stopping..")
        elif(cmd == "screenshot"):
            print("[screenshot] loading")
            filename = datetime.now().strftime('%Y%m%d%H%M%S' + ".png")
            pyautogui.screenshot(filename, region=(110, 140, 770, 525))
            print("[screenshot] saved")
        elif(cmd == "help"):
            help()
        elif(cmd == ""):
            pass
        else:
            print("[error] cmd not found")
            setupWindow(hwnd_console,
                            wdow_xpos + wdow_width,
                            wdow_ypos,
                            wdow_width,
                            wdow_height)
            setupWindow(hwnd,
                    wdow_xpos,
                    wdow_ypos,
                    wdow_width,
                    wdow_height)
        selectWindow(hwnd_console, wdow_console_xpos, wdow_ypos)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("user exiting..")
        exit(0)
