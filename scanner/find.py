import threading
import pyautogui
import time

class pixel_scanner_threads(threading.Thread):
   def __init__(self, thread_id, rgb_pixel, x, y, width, height, image_to_scan):
      threading.Thread.__init__(self)
      self.thread_id = thread_id
      self.rgb_pixel = rgb_pixel
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.image_to_scan = image_to_scan
   def run(self):
      scan_results = pixelScan(self.rgb_pixel, self.x, self.y, self.width, self.height, self.image_to_scan)
      if(scan_results != None):
          self.data = scan_results
      else:
          self.data = None

def pixelScan(rgb_pixel, x, y, width, height, image_to_scan):
    for xi in range(x, x + width):
        for yi in range(y, y + height):
            cur_pixel = image_to_scan.getpixel((xi, yi))
            if(cur_pixel == rgb_pixel):
                return (xi, yi)
            else:
                pass

def startPixelScan(rgb_pixel, x, y, width, height):
    section_width = int(width / 8)
    threads = []
    final_scan = []
    for i in range(8):
        thread_id = str(i)
        image_to_scan = pyautogui.screenshot()
        thread = pixel_scanner_threads(thread_id, rgb_pixel, x, y, section_width, height, image_to_scan)
        x += section_width
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    for thread in threads:
        if thread.data != None:
            final_scan.append(thread.data)
    if(len(final_scan) <= 0):
        print("[warning] could not find pixel")
    else:
        return final_scan


class scanner_threads(threading.Thread):
   def __init__(self, thread_id, image_path, x, y, width, height):
      threading.Thread.__init__(self)
      self.thread_id = thread_id
      self.image_path = image_path
      self.x = x
      self.y = y
      self.width = width
      self.height = height
   def run(self):
      scan_results = scan(self.image_path, self.x, self.y, self.width, self.height)
      if(scan_results):
          self.data = scan_results
      else:
          self.data = None

def scan(image_path, x, y, width, height):
    item_pos = pyautogui.locateAllOnScreen(image_path,region=(x, y, width, height))
    if(item_pos):
        return item_pos
    return None

def startScan(image_path, x, y, width, height):
    section_width = int(width / 4)
    threads = []
    final_scan = []
    for i in range(4):
        thread_id = str(i)
        thread = scanner_threads(thread_id, image_path, x, y, section_width, height)
        x += section_width
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    for thread in threads:
        for pos_set in thread.data:
            final_scan.append(pos_set)
    if(len(final_scan) <= 0):
        print("[warning] could not find %s" % image_path)
    else:
        return final_scan


"""
fpath = "C:/Users/blizire/Desktop/programming/python/osrs/imgs/salmon_block_inventory.png"
x, y, width, height = 662, 334, 190, 264
records = startScan(fpath, x, y, width, height)
for i in records:
    print(i)
"""
if __name__ == "__main__":
    x, y, width, height = 662, 334, 190, 264
    color = (104,225,43)
    results = startPixelScan(color, x, y, width, height)
    for i in results:
        print(i)
