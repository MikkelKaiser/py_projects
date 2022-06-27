from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import config

# Manual chrome version download here
# Download your chrome driver for script here => https://chromedriver.chromium.org/downloads
# PATH = "C:/Users/Mikke/OneDrive/Desktop/Python_project/asd/chrome_driver/chromedriver.exe"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open up site
driver.get("https://suite.adnami.io")

# get email, password and btn input fields
driver.implicitly_wait(5)
email = driver.find_element(By.ID, "Input_Email")
password = driver.find_element(By.ID, "Input_Password")
submit_btn = driver.find_element(By.CLASS_NAME, "btn")

# Throw email into input field
email.send_keys(config.emailadress)
# Throw password into input field
password.send_keys(config.password)
# Submit the login
submit_btn.click()


# After login go to hosting url
time.sleep(2)
driver.get("https://suite.adnami.io/hosting")

# Get desired selected element and dropdown
driver.implicitly_wait(10)
organisation_dropdown = driver.find_elements(By.XPATH, "(//div[@class='multiselect__tags'])[1]")
selectElem = driver.find_element(By.XPATH, "//span[contains(text(),'Adnami Development')]")

# open dropdown
organisation_dropdown[0].click()
# Select 'Adnami Development'
selectElem.click()

# Open second dropdown
# driver.implicitly_wait(2)
second_drop = driver.find_elements(By.XPATH, "(//div[@class='multiselect__tags'])[2]")
second_drop[0].click()

# driver.implicitly_wait(5)
# Select 'Certification Ads'
select_drop2 = driver.find_element(By.XPATH, "//span[contains(text(),'Certification Ads')]")
select_drop2.click()

# Fill in the campaign name
campaign_name = driver.find_element(By.XPATH, "(//input[@type='text'])[4]")
campaign_name.send_keys(" - Hosting")

# campaign_description = driver.find_element(By.ID, 'input-81')
# time.sleep(0.5)
# campaign_description.send_keys("Random desc")
# time.sleep(1)

# country_dropdown = driver.find_element(By.CLASS_NAME, "multiselect.country-filter-input")
# selectCountry =  driver.find_element(By.XPATH, "//span[text()='Denmark']")
# time.sleep(1)
# country_dropdown.click()
# time.sleep(1)
# selectCountry.click()

# Wait time before closing window
time.sleep(40)


