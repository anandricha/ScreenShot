#coding=utf-8
import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options

def test_fullpage_screenshot_desktop_mobile(url,screenshot_name,serial_number,path):
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--start-maximized')
    firefoxoptions = Options()
    # firefox_options.headless = True
    firefoxoptions.add_argument('-headless')
    firefoxoptions.add_argument('-start-maximized')
    # firefoxoptions.add_argument('incognito')
    driver = webdriver.Firefox(options=firefoxoptions)
    # driver = webdriver.Chrome(options=chrome_options,
    #                           executable_path= path+"\\Drivers\\chromedriver.exe")
    try:
        driver.get("about:blank")
        # driver.delete_all_cookies()
        driver.get(url)
        # driver.execute_script('window.localStorage.clear();')
        time.sleep(2)

        #the element with longest height on page
        if (screenshot_name=='_new_url'):
            ele=driver.find_element("xpath", "//div[@class='row footer-container']/p")
        else:
            ele=driver.find_element("xpath", "//div[@class='okdhsfooterright3']")
        location = ele.location
        height = location['y']+200
        print("height of image in desktop",height)
        total_height = height

        driver.set_window_size(1920, total_height)      #the trick

    except WebDriverException as e:
        print(e)
    finally:
        time.sleep(2)
        if (screenshot_name=='_new_url'):
            driver.save_screenshot("screen_shot_desktop" + screenshot_name + ".png")
            print("screenshot saved succesfully - desktop-new  for serial number", serial_number)
        else:
            driver.save_screenshot("screen_shot_desktop" + screenshot_name + ".png")
            print("screenshot saved succesfully - desktop-old  for serial number", serial_number)
            driver.quit()


    if (screenshot_name=='_new_url'):
        try:
            # driver.refresh()
            driver.set_window_size(360, 800)
            # the element with longest height on page
            ele = driver.find_element("xpath", "//div[@class='row footer-container']/p")
            location = ele.location
            total_height = location['y'] + 100
            print("height of image in Mobile", total_height)

            driver.set_window_size(360, total_height)  # the trick
        except WebDriverException as e:
            print(e)
        finally:
            time.sleep(2)
            driver.save_screenshot("screen_shot_mobile" + screenshot_name + ".png")
            print("screenshot saved succesfully - mobile-  for serial number", serial_number)
            driver.quit()



