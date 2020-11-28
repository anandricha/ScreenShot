""" This class accepts the test case name and appends it to
the screen shot name to generate unique screenshot file name for everytest."""

from datetime import datetime
import time

class ScreenShot():

    def __init__(self,driver):
        self.driver = driver

    def take_screenshot(self,test_case_name : str):
        time_now = time.strftime('%H-%M-%S')
        screen_shot_file_name = test_case_name+ '-'+ time_now
        self.driver.get_screenshot_as_file('C:/Users/hcl60176/PycharmProjects/PDF-UTILITY/Sauce_Demo/Result/Screenshot/'+screen_shot_file_name+'.png')
