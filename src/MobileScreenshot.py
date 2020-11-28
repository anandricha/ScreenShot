#coding=utf-8
import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

def test_fullpage_screenshot_mobile(url,screenshot_name,serial_number,path):
    # chrome_options = Options()
    # chrome_options.add_argument('incognito')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--start-maximized')
    # driver = webdriver.Chrome(
    #     options=chrome_options,
    #     executable_path="C:\\Users\\hcl60176\\PycharmProjects\\URL-PDF\\Drivers\\chromedriver.exe")

    firefoxoptions = Options()
    firefoxoptions.add_argument('-headless')
    firefoxoptions.add_argument('-start-maximized')
    driver = webdriver.Firefox(options=firefoxoptions)

    try:
        driver.get("about:blank")
        driver.delete_all_cookies()
        driver.get(url)
        driver.execute_script('window.localStorage.clear();')
        time.sleep(2)
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
        driver.save_screenshot("screen_shot_mobile"+ screenshot_name + ".png" )
        print("screenshot saved succesfully - desktop  for serial number", serial_number)
        driver.quit()
        time.sleep(1)

