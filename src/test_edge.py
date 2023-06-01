'''This script will run the tests on edge
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities

if __name__ == "__main__":
        edge_options = webdriver.EdgeOptions()
        utilities.set_options(edge_options)  
        #Configure the driver
        edge_driver = utilities.setup_driver(edge_options)
        utilities.ui_test(edge_driver)

