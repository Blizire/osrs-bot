from osrs_buttons import buttons
from rs_data import item
import pyautogui
import time

# inventory slot positions _OBSOLETE_
origin_slot_pos_x, origin_slot_pos_y = 692, 360
ydistance = 36
xdistance = 43
inventory_slot = {
                0:[origin_slot_pos_x, origin_slot_pos_y],
                1:[origin_slot_pos_x, origin_slot_pos_y + (ydistance * 1)],
                2:[origin_slot_pos_x, origin_slot_pos_y + (ydistance * 2)],
                3:[origin_slot_pos_x, origin_slot_pos_y + (ydistance * 3)],
                4:[origin_slot_pos_x, origin_slot_pos_y + (ydistance * 4)],
                5:[origin_slot_pos_x, origin_slot_pos_y + (ydistance * 5)],
                6:[origin_slot_pos_x, origin_slot_pos_y + (ydistance * 6)],
                # row 2
                7:[origin_slot_pos_x + (xdistance * 1), origin_slot_pos_y],
                8:[origin_slot_pos_x + (xdistance * 1), origin_slot_pos_y + (ydistance * 1)],
                9:[origin_slot_pos_x + (xdistance * 1), origin_slot_pos_y + (ydistance * 2)],
                10:[origin_slot_pos_x + (xdistance * 1), origin_slot_pos_y + (ydistance * 3)],
                11:[origin_slot_pos_x + (xdistance * 1), origin_slot_pos_y + (ydistance * 4)],
                12:[origin_slot_pos_x + (xdistance * 1), origin_slot_pos_y + (ydistance * 5)],
                13:[origin_slot_pos_x + (xdistance * 1), origin_slot_pos_y + (ydistance * 6)],
                # row 3
                14:[origin_slot_pos_x + (xdistance * 2), origin_slot_pos_y],
                15:[origin_slot_pos_x + (xdistance * 2), origin_slot_pos_y + (ydistance * 1)],
                16:[origin_slot_pos_x + (xdistance * 2), origin_slot_pos_y + (ydistance * 2)],
                17:[origin_slot_pos_x + (xdistance * 2), origin_slot_pos_y + (ydistance * 3)],
                18:[origin_slot_pos_x + (xdistance * 2), origin_slot_pos_y + (ydistance * 4)],
                19:[origin_slot_pos_x + (xdistance * 2), origin_slot_pos_y + (ydistance * 5)],
                20:[origin_slot_pos_x + (xdistance * 2), origin_slot_pos_y + (ydistance * 6)],
                # row 4
                21:[origin_slot_pos_x + (xdistance * 3), origin_slot_pos_y],
                22:[origin_slot_pos_x + (xdistance * 3), origin_slot_pos_y + (ydistance * 1)],
                23:[origin_slot_pos_x + (xdistance * 3), origin_slot_pos_y + (ydistance * 2)],
                24:[origin_slot_pos_x + (xdistance * 3), origin_slot_pos_y + (ydistance * 3)],
                25:[origin_slot_pos_x + (xdistance * 3), origin_slot_pos_y + (ydistance * 4)],
                26:[origin_slot_pos_x + (xdistance * 3), origin_slot_pos_y + (ydistance * 5)],
                27:[origin_slot_pos_x + (xdistance * 3), origin_slot_pos_y + (ydistance * 6)],
}

inventory_icon_pos = (756, 314)

# returns tuples with positions of found items
def scanInventory(item_name):
    inv_icon_x, inv_icon_y = inventory_icon_pos
    pyautogui.click(inv_icon_x, inv_icon_y)
    inv_start_x, inv_start_y = 662, 334
    inv_width, inv_height = 190, 264
    item_image = item.item_dict[item_name]
    item_pos = pyautogui.locateAllOnScreen(item_image,region=(inv_start_x, inv_start_y,
                                                                inv_width, inv_height))
    if(item_pos != None):
        return item_pos
    else:
        print("[warning] couldn't find %s" % item)
        return 0

# input scanInventory positions to drop items in that position
def dropItems(scanned_pos):
    inv_icon_x, inv_icon_y = inventory_icon_pos
    for item_pos in scanned_pos:
        pyautogui.click(inv_icon_x, inv_icon_y)
        x, y, w, h = item_pos
        pyautogui.moveTo(x,y)
        pyautogui.click(button="right")
        xdrop, ydrop = pyautogui.locateCenterOnScreen(buttons.button_paths["drop"], grayscale=True, region=(x-100, y, 200, 100))
        pyautogui.moveTo(xdrop,ydrop)
        pyautogui.click(button="left")


def quickDrop(item_name):
    #check item is in item list
    for item_check in item.item_dict:
        if(item_check == item_name):
            items_pos = scanInventory(item_name)
            if(items_pos):
                dropItems(items_pos)
            else:
                break;


def bury(scanned_pos):
    inv_icon_x, inv_icon_y = inventory_icon_pos
    for item_pos in scanned_pos:
        pyautogui.click(inv_icon_x, inv_icon_y)
        x, y, w, h = item_pos
        time.sleep(0.6)
        pyautogui.moveTo(x,y)
        pyautogui.click(button="left")

def quickBury():
    while True:
        items_list = []
        items_pos = scanInventory("bone")
        for i in items_pos:
            items_list.append(i)
        if not(len(items_list)):
            break
        bury(items_list)
