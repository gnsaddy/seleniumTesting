from selenium import webdriver as wb

# relative and absolute path for giving the path of browser drivers
# defining the relative path for chromedriver
driver = wb.Chrome("../Drivers/x32/chromedriver.exe")

# launching the url using get
driver.get("https://www.seleniumeasy.com/")
