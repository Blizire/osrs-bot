from osrs_buttons import inventory
from osrs_buttons import buttons
from rs_data import item
import pyautogui
import time

# returns tuples with positions of found items
def scanInventory(item_name):
    inv_icon_x, inv_icon_y = inventory.inventory_icon_pos
    pyautogui.click(inv_icon_x, inv_icon_y)
    inv_start_x, inv_start_y = 662, 334
    inv_width, inv_height = 190, 264
    item_image = item.item_dict[item_name]
    item_pos = pyautogui.locateAllOnScreen(item_image,region=(inv_start_x, inv_start_y,
                                                                inv_width, inv_height))
    if(item_pos):
        return item_pos
    else:
        print("[warning] couldn't find %s" % item)
        return None

# input scanInventory positions to drop items in that position
def dropItems(scanned_pos):
    inv_icon_x, inv_icon_y = inventory.inventory_icon_pos
    for item_pos in scanned_pos:
        pyautogui.click(inv_icon_x, inv_icon_y)
        x, y, w, h = item_pos
        pyautogui.moveTo(x,y)
        pyautogui.click(button="right")
        xdrop, ydrop = pyautogui.locateCenterOnScreen(buttons.button_paths["drop"], grayscale=True, region=(x-100, y, 200, 100))
        pyautogui.moveTo(xdrop,ydrop)
        pyautogui.click(button="left")

stuff = scanInventory("raw trout")
dropItems(stuff)
