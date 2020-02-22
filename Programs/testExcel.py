import os
import time
import xlrd
from selenium import webdriver

my_path = os.path.abspath(os.path.dirname(__file__))
drivePath = os.path.join(my_path, "../Drivers/x32/chromeDriver.exe")
excelPath = os.path.join(my_path, "../excel/TestData.xls")

driver = webdriver.Chrome(drivePath)
# maximaize window
driver.maximize_window()
time.sleep(1)

driver.get("https://www.facebook.com")
time.sleep(1)
email = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")

loginBtn = driver.find_element_by_css_selector("input[type='submit']")

excelBook = xlrd.open_workbook(excelPath)
ws = excelBook.sheet_by_index(0)
username = ws.cell_value(1, 0)
passExcel = ws.cell_value(1, 1)

email.send_keys(username)
password.send_keys(str(passExcel))

time.sleep(1)
timeStr = time.strftime("%Y%m%d = %H%M%S")
sImage = "webImages"

# taking screenshots
driver.save_screenshot("../screenShots/"+sImage+timeStr+".png")
loginBtn.click()




