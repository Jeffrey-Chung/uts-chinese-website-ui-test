'''This script has all my tests on it and will be imported to test_uts_chinese_website. It will also be tested on my local machine 
and not run on GitHub Actions
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



firefox_options = webdriver.FirefoxOptions()


#Headless option for github action
#firefox_options.add_argument("--headless")

firefox_options.add_argument("--kiosk") # Firefox is not chromium!!!  


#Configure the driver
firefox_driver = webdriver.Remote( 
command_executor="http://localhost:4444",
options=firefox_options
)

firefox_driver.get('https://utsaustralia.cn/') #Fire up the Fox Cannon!

#Fills in the details of the contact form, each variable represents each field
def fill_survey(driver):
                action_chain = ActionChains(driver)
                '''This code onwards can only be run in non-headless mode'''
                name = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[1]/span/input'))
        ).send_keys("Jane Smith")
                #action_chain.move_to_element(name).send_keys("Jane Smith").perform()
                
                contact_number = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[2]/span/input'))
        ).send_keys("0432 995 543")
                #action_chain.move_to_element(contact_number).send_keys("0432 995 543").perform()
                email = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[3]/span/input'))
        ).send_keys("svcbnmjhtgfd@gmail.com")
                #action_chain.move_to_element(email).send_keys("svcbnmjhtgfd@gmail.com").perform()

                year_2_option = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[4]/span/select/option[2]"))).click()

                enquiry_text = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[9]/span/textarea'))
        ).send_keys("THIS IS JUST FOR TESTING")
                
                captcha = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[10]/span/input'))
        ).send_keys("1234")
                
                age_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div[1]/div/form/div[2]/div[12]/span/span/span/label/input'))
        )
                driver.execute_script("arguments[0].click();", age_checkbox)
                driver.back()
                



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
                #driver.implicitly_wait(120)
                #Arrow keys are not visible in google chrome
                circle_icon_addresses = []
                for dot_numbers in range(1, 5):
                        address = f"/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/ss3-force-full-width/div/div[1]/div/div/div/div[2]/div[3]/div/div[{dot_numbers}]/div"
                        circle_icon_addresses.append(address)
                for circle_icon_address in circle_icon_addresses:
                        circle_icon = driver.find_element(By.XPATH, circle_icon_address)
                        driver.execute_script("arguments[0].click();", circle_icon)
                        #action_chain.move_to_element(circle_icon).click().perform()
                
                        
                
                #This will hover to the video area but won't do anything
                video = driver.find_element(By.XPATH, '/html/body/div/div[1]')
                action_chain.move_to_element(video).click().perform()
                
                '''The code block is commented below because the video is blocked in the grid servers=     
                play_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div[1]/button[1]'))
        )
                action_chain.move_to_element(play_button).click().perform()
                '''
                
                faculty_and_course_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[4]/div/a/div/div[1]/picture/img').click()
                
                #Page may take a long time to fully load and render, if it takes > 2mins it will throw an error
                driver.implicitly_wait(120)
                contact_form_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/main/div/article/div/div/div[1]/div/div/div[2]/a[1]'))
        ).click()
               
                fill_survey(driver)
                driver.back()
                world_rankings_button = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/main/div/article/div/div/div[5]/div/a/div/div[1]/picture/img"))
        ).click()
                #Clicks on the course pathway side bar at the top of each page
                pathway_sidebar = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/header/div/div/nav/ul/li[4]"))
        ).click()
                #Clicks on the how to apply side bar at the top of each page
                how_to_apply_sidebar = WebDriverWait(driver, 40).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/header/div/div/nav/ul/li[5]"))
        ).click()
                 #Clicks on the uts news side bar at the top of each page
                uts_news_sidebar = WebDriverWait(driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[4]/header/div/div/nav/ul/li[6]"))
        ).click()
                
                #Search "uts" on the search bar
                search_icon = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.ID, "search_switch_button"))
        ).click()
                
                search_text_field = WebDriverWait(driver, 30).until(
                        EC.visibility_of_element_located((By.ID, "search"))
                ).send_keys("uts")
                
                submit_search = WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="search_submit"]'))
        ).click()
                
                #Go back to the original loaded page to finish the test
                uts_icon = WebDriverWait(driver, 30).until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="utsFixedTopBar"]/div/div/div[1]/a/img'))
                ).click()
        
        finally:
                #prints the url that was last loaded
                print(driver.current_url)
                driver.quit()

if __name__ == "__main__":
        ui_test(firefox_driver)

