from selenium import webdriver as wb

# relative and absolute path for giving the path of browser drivers
# defining the relative path for firefox driver

driver = wb.Firefox(executable_path="../Drivers/x64/geckodriver.exe")

# launching the url using get
driver.get("https://www.seleniumeasy.com/")
