import pyautogui
from time import sleep

def print_recorded_data(data):
    for i in data:
        mouse_id = i[0]
        mouse_pos = i[1]
        mouse_rgb = i[2]
        print("[id:%s, pos:%s, rgb:%s]" % (mouse_id, mouse_pos, mouse_rgb))

def write_recorded_data(data, data_filename):
    data_file = open(data_filename ,'w')
    for i in data:
        mouse_id = i[0]
        mouse_pos_x, mouse_pos_y = i[1]
        mouse_rgb_r, mouse_rgb_g, mouse_rgb_b = i[2]
        data_file.write("id:%s/pos:%s,%s/rgb:%s,%s,%s\n" % (mouse_id, mouse_pos_x, mouse_pos_y, mouse_rgb_r, mouse_rgb_g, mouse_rgb_b))
    data_file.close()
    print("[recorded-data] written to %s" % data_filename)

def start():
    data_filename = "mouse_data.txt"
    recorded_data = []
    wait_time = 1
    count = 0
    try:
        while(True):
            count += 1
            sleep(wait_time)
            mouse_id = count
            xpos_mouse, ypos_mouse = pyautogui.position()
            r_mouse_pixel, g_mouse_pixel, b_mouse_pixel = pyautogui.pixel(xpos_mouse, ypos_mouse)
            recorded_data.append([mouse_id, [xpos_mouse, ypos_mouse], [r_mouse_pixel, g_mouse_pixel, b_mouse_pixel]])
            print("[mouse-id] %s" % mouse_id)
            print("\t|_[mouse-pos] x:%s y:%s" % (xpos_mouse, ypos_mouse))
            print("\t|_[pixel-info] RGB(%s,%s,%s)" % (r_mouse_pixel, g_mouse_pixel, b_mouse_pixel))
            print("\t|")
    except KeyboardInterrupt:
        write_recorded_data(recorded_data, data_filename)

def main():
    data_filename = "mouse_data.txt"
    recorded_data = []
    wait_time = 1
    count = 0
    try:
        while(True):
            count += 1
            sleep(wait_time)
            mouse_id = count
            xpos_mouse, ypos_mouse = pyautogui.position()
            r_mouse_pixel, g_mouse_pixel, b_mouse_pixel = pyautogui.pixel(xpos_mouse, ypos_mouse)
            recorded_data.append([mouse_id, [xpos_mouse, ypos_mouse], [r_mouse_pixel, g_mouse_pixel, b_mouse_pixel]])
            print("[mouse-id] %s" % mouse_id)
            print("\t|_[mouse-pos] x:%s y:%s" % (xpos_mouse, ypos_mouse))
            print("\t|_[pixel-info] RGB(%s,%s,%s)" % (r_mouse_pixel, g_mouse_pixel, b_mouse_pixel))
            print("\t|")
    except KeyboardInterrupt:
        write_recorded_data(recorded_data, data_filename)
        return None


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("user exiting..")
