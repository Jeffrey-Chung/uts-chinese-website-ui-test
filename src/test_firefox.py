'''This script will run the tests on firefox
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities

if __name__ == "__main__":
        firefox_options = webdriver.FirefoxOptions()
        utilities.set_options(firefox_options)  
        #Configure the driver
        firefox_driver = utilities.setup_driver(firefox_options)
        utilities.ui_test(firefox_driver)

