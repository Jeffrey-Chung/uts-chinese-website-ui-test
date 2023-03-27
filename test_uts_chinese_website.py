from selenium import webdriver
from draft_tests_uts_chinese_website import ui_test

# define ze options
firefox_options = webdriver.FirefoxOptions()
chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()

#chrome_options.add_argument("--disable-dev-shm-usage")

#function to set same options for each browser
def set_options(driver_options):
        #driver_options.add_argument("--headless")
        driver_options.add_argument("--ignore-certificate-errors")
        driver_options.add_argument("--kiosk")

set_options(firefox_options)
set_options(chrome_options)
set_options(edge_options)

#Function to configure settings for each driver
def setup_driver(driver_options):
        driver = webdriver.Remote( 
        command_executor="http://localhost:4444",
        options=driver_options
        )

        #Load the uts website
        driver.get('https://utsaustralia.cn/')
        return driver

firefox_driver = setup_driver(firefox_options)
chrome_driver = setup_driver(chrome_options)
edge_driver = setup_driver(edge_options)


if __name__ == "__main__":
        ui_test(firefox_driver)
        ui_test(chrome_driver)
        ui_test(edge_driver)
