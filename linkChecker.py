import time
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from htmldom import htmldom

from selenium.webdriver.firefox.options import Options
print("start test")

def intitialize_driver():
    print("inside the def ")
    driver = webdriver.Chrome(executable_path="C:\\Users\\hcl60176\\PycharmProjects\\URL-PDF\\Drivers\\chromedriver.exe")
    url = "https://aem-qa.ok.gov/okdrs"
    return driver, url


def link_checker():
    driver,url = intitialize_driver()
    try:
        driver.get("about:blank")
        # driver.delete_all_cookies()
        driver.get(url)
    except WebDriverException as e:
        print(e)
    finally:
        links_on_page = driver.find_elements_by_tag_name('a')
        print(len(links_on_page))
        # for links in links_on_page:
        #     print(links.get_attribute("href"))


def link_checker_using_dom():
    url = "https://aem-qa.ok.gov/okdrs"
    try:
        dom = htmldom.HtmlDom(url)
        dom.createDom()
        all_links = dom.find("a")
        for links in all_links:
            print(links.attr("href"))
        print("--------------------------------------------------------------------------------------------------------")
        all_images = dom.find("img")
        for images in all_images:
            print(images.attr("src"))
    except Exception as e:
        print(e)

link_checker_using_dom()

