#coding=utf-8
import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from Lib.DataGenerator import data_generator_return__nested_list
import os
path = os.getcwd()


def test_fullpage_screenshot_mobile():
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--start-maximized')


    full_path = path + "\\URL.xlsx"
    print(full_path)
    data = data_generator_return__nested_list(full_path, 'Sheet1')
    print(data)
    data1 = data.reverse()
    print(data1)
    firefoxoptions = Options()
    firefoxoptions.add_argument('-headless')
    firefoxoptions.add_argument('-start-maximized')
    driver = webdriver.Firefox(options=firefoxoptions)


    for each_item in range(300):
        try:
            driver.get("about:blank")
            driver.delete_all_cookies()
            driver.get(data[each_item][1])
            driver.execute_script('window.localStorage.clear();')
            driver.refresh()
            time.sleep(3)
            driver.set_window_size(360, 800)
            #the element with longest height on page

            ele = driver.find_element("xpath", "//div[@class='row footer-container']/p")
            location = ele.location
            total_height = location['y']+100
            print("height of image in Mobile", total_height)

            driver.set_window_size(360, total_height)      #the trick
        except WebDriverException as e:
            print(e)
        finally:
            time.sleep(2)
            print("screenshot saved succesfully - desktop  for serial number", data[each_item][1])
            driver.execute_script('window.localStorage.clear();')
            driver.quit()
            time.sleep(1)

if __name__ == '__main__':
    test_fullpage_screenshot_mobile()



