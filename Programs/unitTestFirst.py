import os
import unittest
import time

from selenium import webdriver

chromeDriver = "../Drivers/x32/chromedriver.exe"


class ChromeLaunch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromeDriver)
        driver = self.driver
        time.sleep(3)
        driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("https://www.google.co.in/")
        textBox = self.driver.find_element_by_name("q")
        textBox.send_keys("Hello google")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
