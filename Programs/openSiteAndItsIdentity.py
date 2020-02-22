import time

from selenium import webdriver as wb

timeStr = time.strftime("%Y%m%d = %H%M%S")
# relative and absolute path for giving the path of browser drivers
# defining the relative path for chromedriver
driver = wb.Chrome("../Drivers/x32/chromedriver.exe")
# maximaize window
driver.maximize_window()

# launching the url using get
driver.get("https://www.google.co.in/")
# id, name, css selector, xpath

# searchBox = driver.find_element_by_css_selector("input[title = 'Search']")

# using xpath

searchBoxPath = driver.find_element_by_xpath("//input[@role='combobox']")
# sending request to search in search bar
searchBoxPath.send_keys("Selenium easy")
time.sleep(1)
sImage = "webImages"

# taking screenshots
driver.save_screenshot("../screenShots/"+sImage+timeStr+".png")



driver.find_element_by_id("lga")
searchButtom = driver.find_element_by_css_selector("input[type='submit']")
# using xPath
# searchButtom = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")
searchButtom.click()
# working with xPath
# searchButtom.send_keys()

# for searching into google checkbox, directly search if only one search box is there
# searchBoxPath.submit()

# to search in next page link
nextSearch = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/div[1]/a/h3")
time.sleep(1)
nextSearch.click()


searchToNg = driver.find_element_by_xpath("//*[@id='navbar-collapse']/nav/ul/li[3]/a")
time.sleep(1)
searchToNg.click()
