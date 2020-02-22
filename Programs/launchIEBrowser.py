from selenium import webdriver as wb
import os

# relative and absolute path for giving the path of browser drivers
# defining the relative path for firefox driver

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x64/IEDriverServer.exe")

driver = wb.Ie(path)

# launching the url using get
driver.get("https://www.seleniumeasy.com/")
