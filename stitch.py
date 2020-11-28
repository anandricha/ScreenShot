from Lib.DataGenerator import data_generator_return__nested_list
import os
from src.DesktopScreenshot import test_fullpage_screenshot_desktop_mobile
# from src.MobileScreenshot import test_fullpage_screenshot_mobile
from PIL import Image
import time
from datetime import datetime
from selenium.common.exceptions import WebDriverException

path = os.getcwd()
print(path)
full_path = path + "//URL.xlsx"
data = data_generator_return__nested_list(
    full_path, 'Sheet1')
#  reverse the list to star from 1
data.reverse()
print('executing screenshot for ',data[0])
items_in_sheet = len(data)
print(items_in_sheet)

start = datetime.now()
print("----------start time -------------",start)
for each_item in range(items_in_sheet):
    print("starting screenshot creation for serial number ",data[each_item][0])
    # create full page screenshots and save
    try:
        test_fullpage_screenshot_desktop_mobile(data[each_item][1], "_new_url",data[each_item][0],path)
    except WebDriverException as e:
            print(e)

    try:
        test_fullpage_screenshot_desktop_mobile(data[each_item][2], "_old_url",data[each_item][0],path)
    except WebDriverException as e:
            print(e)

    # try:
    #     test_fullpage_screenshot_mobile(data[each_item][1], "_new_url",data[each_item][0],path)
    # except WebDriverException as e:
    #         print(e)
    # "screen_shot_desktop_old_url.png",

    files = ["screen_shot_desktop_new_url.png",
             "screen_shot_desktop_old_url.png",
             "screen_shot_mobile_new_url.png"]

    images = [Image.open(x) for x in files]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)+100
    max_height = max(heights)
    # creating a new blank image with total width and max height
    new_im = Image.new('RGB', (total_width, max_height))

    # Pasting each image after previous image
    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]
    # appending sheet serial number to image name for mapping
    serial_number_sheet = str(data[each_item][0])
    filename = 'Screenshot_latest_on_pod'+serial_number_sheet+'.jpg'
    new_im.save(filename)
    print('file created for ----',filename)
    time.sleep(2)
end = datetime.now()
print("-----------execution ended---------------",end)
print ("total time  is --------------", end-start)


