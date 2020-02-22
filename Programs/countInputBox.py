from selenium import webdriver
import os

driver = webdriver.Firefox(executable_path="../Drivers/x64/geckodriver.exe")
driver.get("https://www.facebook.com/")

radio = driver.find_elements_by_css_selector("input[name='sex']")
count = 0

for i in radio:
    count += 1

print("radio button count = ", count)
driver.quit()
