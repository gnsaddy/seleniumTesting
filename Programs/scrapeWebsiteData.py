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

# launching the url using get
driver.get("https://www.google.co.in/")
# id, name, css selector, xpath
# searchBox = driver.find_element_by_css_selector("input[title = 'Search']")
# using xpath
searchBoxPath = driver.find_element_by_xpath("//input[@role='combobox']")
# sending request to search in search bar
searchBoxPath.send_keys("Selenium easy demo website")
time.sleep(1)
sImage = "webImages"
# taking screenshots
driver.save_screenshot("../screenShots/" + sImage + timeStr + ".png")
driver.find_element_by_id("lga")
searchButtom = driver.find_element_by_css_selector("input[type='submit']")
# using xPath
# searchButtom = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")
searchButtom.click()
getText = driver.find_element_by_css_selector("#rso > div:nth-child(1) >"
                                              " div > div > table > tbody > "
                                              "tr.mslg.dmenKe > td:nth-child(1) > div > span > h3 > a")

valueFetched = getText.text
print(valueFetched)


# # fetch and store in new workbook
# wb = xlwt.Workbook()
# ws = wb.add_sheet("Sheet 1")
# ws.write(0, 0, valueFetched)
# wb.save(excelPath+"/fetchFile.xls")



# to update in excel book
wb = copy(xlrd.open_workbook(excelPath + "/fetchFile.xls"))
wb.get_sheet(0).write(3, 3, valueFetched)
wb.save(excelPath+"/fetchFile.xls")
