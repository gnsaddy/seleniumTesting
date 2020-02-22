import time
import xlrd
from copy import copy

from selenium import webdriver

timeStr = time.strftime("%Y%m%d = %H%M%S")
excelPath = "../excel/"
# relative and absolute path for giving the path of browser drivers
# defining the relative path for chromedriver
driver = webdriver.Chrome("../Drivers/x32/chromedriver.exe")
# maximaize window
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
# clickBtn = driver.find_element_by_css_selector("button[onclick='myAlertFunction\(\)']")
#
# clickBtn.click()
# alertJS = driver.switch_to.alert
# print(alertJS.text)
# alertJS.accept()


clickBtnCancel = driver.find_element_by_css_selector("#easycont > div > div.col-md-6.text-left >"
                                                     " div:nth-child(5) > div.panel-body > button")
clickBtnCancel.click()
# cancel
alertCancel = driver.switch_to.alert
print(alertCancel.text)
time.sleep(5)
alertCancel.dismiss()
