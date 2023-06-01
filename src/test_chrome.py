'''This script will run the tests on chrome
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities

if __name__ == "__main__":
        chrome_options = webdriver.ChromeOptions()
        utilities.set_options(chrome_options)  
        #Configure the driver
        chrome_driver = utilities.setup_driver(chrome_options)
        utilities.ui_test(chrome_driver)

