from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from draft_tests_uts_chinese_website import ui_test

# define ze options
firefox_options = webdriver.FirefoxOptions()
chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()

# Headless option for github action
#firefox_options.add_argument("--headless")
#chrome_options.add_argument("--headless")
#edge_options.add_argument("--headless")

#chrome_options.add_argument("--disable-dev-shm-usage")

#firefox_options.add_argument("--kiosk") # Firefox is not chromium!!!  
#chrome_options.add_argument("--kiosk")
#edge_options.add_argument("--kiosk")

# Set executor and firefox options
firefox_driver = webdriver.Remote( 
command_executor="http://localhost:4444",
options=firefox_options
)

# Set executor and chrome options
chrome_driver = webdriver.Remote( 
command_executor="http://localhost:4444",
options=chrome_options
)

# Set executor and edge options
edge_driver = webdriver.Remote( 
command_executor="http://localhost:4444",
options=edge_options
)

#Load the uts website
firefox_driver.get('https://utsaustralia.cn/') 
chrome_driver.get('https://utsaustralia.cn/')  
edge_driver.get('https://utsaustralia.cn/')  
 

if __name__ == "__main__":
        ui_test(firefox_driver)
        ui_test(chrome_driver)
        ui_test(edge_driver)
