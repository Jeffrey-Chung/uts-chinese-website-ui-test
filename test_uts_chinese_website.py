from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# define ze options
firefox_options = webdriver.FirefoxOptions()
chrome_options = webdriver.ChromeOptions()
edge_options = webdriver.EdgeOptions()

# Headless option for github action
firefox_options.add_argument("--headless")
chrome_options.add_argument("--headless")
edge_options.add_argument("--headless")

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
 

def ui_test(driver):
        #Check if the website has a valid certificate by starting with http://
        if driver.current_url.startswith('https://'):
                print("The website has a valid certificate.")
        else:
                print("The website does not have a valid certificate.")
        action_chain = ActionChains(driver)
        '''For whatever reason, github action is not able to find the right and left arrow key element'''
        #right_arrow_key = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div/ss3-force-full-width/div/div[1]/div/div/div/div[2]/div[2]/img').click()
        #left_arrow_key = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div/ss3-force-full-width/div/div[1]/div/div/div/div[2]/div[4]/img').click()
        faculty_and_course_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[4]/div/a/div/div[1]/picture/img').click()
        video = driver.find_element(By.XPATH, '/html/body/div/div[1]')
        action_chain.move_to_element(video).perform()
        driver.quit()

if __name__ == "__main__":
        ui_test(firefox_driver)
        ui_test(chrome_driver)
        ui_test(edge_driver)
