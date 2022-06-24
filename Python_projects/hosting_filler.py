from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import config

# Manual chrome version download here
# Download your chrome driver for script here => https://chromedriver.chromium.org/downloads
# PATH = "C:/Users/Mikke/OneDrive/Desktop/Python_project/asd/chrome_driver/chromedriver.exe"

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open up site
driver.get("https://suite.adnami.io")
# wait 1 second
time.sleep(2)

# get email, password and btn input fields
email = driver.find_element(By.ID, "Input_Email")
password = driver.find_element(By.ID, "Input_Password")
submit_btn = driver.find_element(By.CLASS_NAME, "btn")

# Throw email into input field
email.send_keys(config.emailadress)
# Throw password into input field
password.send_keys(config.password)
# Submit the login
submit_btn.click()
time.sleep(2)

# After login go to hosting url
driver.get("https://suite.adnami.io/hosting")
time.sleep(2)

# Get desired selected element and dropdown
organisation_dropdown = driver.find_elements(By.CLASS_NAME, "multiselect.organization-filter-input")
selectElem = driver.find_element(By.XPATH, "//span[text()='Adnami Development']")
time.sleep(1)
# open dropdown
organisation_dropdown[0].click()
time.sleep(0.5)
# Select 'Adnami Development'
selectElem.click()
time.sleep(1)

# Open second dropdown
organisation_dropdown[1].click()
time.sleep(1)
# Select 'Certification Ads'
selectFilter = driver.find_element(By.XPATH, "//span[text()='Certification Ads']")
selectFilter.click()
time.sleep(2)

# Fill in the campaign name
campaign_name = driver.find_element(By.ID, 'input-77')
campaign_name.send_keys(" - Hosting")

# Wait time before closing window
time.sleep(40)


