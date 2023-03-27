'''This script is purely to try out tests to be run on test_uts_chinese_website script as I have not installed chrome
and edge on my local machine
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# define ze options
firefox_options = webdriver.FirefoxOptions()


# Headless option for github action
firefox_options.add_argument("--headless")

firefox_options.add_argument("--kiosk") # Firefox is not chromium!!!  


# Point me in the right direction baby!
firefox_driver = webdriver.Remote( 
command_executor="http://localhost:4444",
options=firefox_options
)



firefox_driver.get('https://utsaustralia.cn/') #Fire up the Fox Cannon!

 
# Run deez tests!
def ui_test(driver):
        try:
                #Check if the website has a valid certificate by starting with http://
                if driver.current_url.startswith('https://'):
                        print("The website has a valid certificate.")
                else:
                        print("The website does not have a valid certificate.")
                action_chain = ActionChains(driver)
        
                #Page may take a long time to fully load and render, if it takes > 2mins it will throw an error
                driver.implicitly_wait(120)
                #Arrow keys are not visible in google chrome
                for dot_numbers in range(5):
                        circle_icon = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div/ss3-force-full-width/div/div[1]/div/div/div/div[2]/div[3]/div/div[' + str(dot_numbers+1)+ ']/div'))
        )
                        action_chain.move_to_element(circle_icon).click().perform()
                
                #This will hover to the video area but won't do anything
                video = driver.find_element(By.XPATH, '/html/body/div/div[1]')
                action_chain.move_to_element(video).click().perform()
                '''The video in the commented code block below  is blocked in the grid servers, therefore code is commented        
                play_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div[1]/button[1]'))
        )
                action_chain.move_to_element(play_button).click().perform()
                '''
                
                faculty_and_course_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[4]/div/a/div/div[1]/picture/img').click()
                contact_form_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div/div/div[2]/a[1]')
                action_chain.move_to_element(contact_form_button).click().perform()
                 
                #Fills in the details of the contact form, each variable represents each field
                name = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[1]/span/input').send_keys("Jane Smith").perform()
                #action_chain.move_to_element(name)
                contact_number = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[2]/span/input').send_keys("0432 995 543")
                #action_chain.move_to_element(contact_number).send_keys("0432 995 543").perform()
                email = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[3]/span/input').send_keys("svcbnmjhtgfd@gmail.com")
                #action_chain.move_to_element(email).send_keys("svcbnmjhtgfd@gmail.com").perform()
                school_year_dropdown_bar = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[4]/span/select').click()
                #action_chain.move_to_element(school_year_dropdown_bar).click().perform()
                year_2_button = driver.find_element(By.XPATH, f'/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[4]/span/select/option[2]').click()
                #action_chain.move_to_element(year_2_button).click().perform()

        finally:
                driver.quit()
        
if __name__ == "__main__":
        ui_test(firefox_driver)

