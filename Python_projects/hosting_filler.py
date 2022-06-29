from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config
import glob

# Manual chrome version download here
# Download your chrome driver for script here => https://chromedriver.chromium.org/downloads

file_path = glob.glob('C:/Users/MikkelAndersen/Desktop/Hosting/*.zip')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open up suite
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

# After login go to hosting url and wait 2 seconds for site load
time.sleep(2)
driver.get("https://suite.adnami.io/hosting")

# Get organisation dropdown
try:

    organisation_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "(//div[@class='multiselect__tags'])[1]"))
    )
finally:
    # open dropdown
    organisation_dropdown.click()

    # Get dropdown option 'Adnami Development'
    selectElem = driver.find_element(
        By.XPATH, "//span[contains(text(),'Adnami Development')]")
    # Select the option
    selectElem.click()

    # driver.implicitly_wait(10)
    # Open second dropdown
    second_drop = driver.find_elements(
        By.XPATH, "(//div[@class='multiselect__tags'])[2]")
    second_drop[0].click()

try:
    # Get 'Certification Ads'
    select_drop2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(text(),'Certification Ads')]"))
    )
    select_drop2.click()

finally:
    # Fill in the campaign name
    campaign_name = driver.find_element(By.XPATH, "(//input[@type='text'])[4]")
    campaign_name.send_keys(" - Hosting")

    # Fill in the description
    campaign_description = driver.find_element(By.XPATH, "(//textarea)[1]")
    campaign_description.send_keys("Random desc")

    # Select Denmark for country
    country_dropdown = driver.find_element(
        By.XPATH, "(//div[@class='multiselect__tags'])[3]")
    selectCountry = driver.find_element(
        By.XPATH, "//span[contains(text(),'Denmark')]")
    country_dropdown.click()
    selectCountry.click()

    # Fill in width and height
    width = driver.find_element(By.XPATH, "(//input[@type='text'])[6]")
    width.send_keys("1000")
    height = driver.find_element(By.XPATH, "(//input[@type='text'])[7]")
    height.send_keys("1000")

    # Click save button to get upload box
    save_btn = driver.find_element(
        By.XPATH, "(//button[@class='ml-6 v-btn v-btn--contained theme--dark v-size--default success'])[1]")
    save_btn.click()

    # Upload zip-file to form
    # Add js code
    remove_styling_from = driver.find_element(
        By.XPATH, "//input[@accept='image/*']")
    driver.execute_script(
        "arguments[0].style.cssText = 'opacity: unset; width:unset; max-width:unset;'", remove_styling_from)

    zip_upload = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//input[@accept='image/*']"))
    )

    zip_upload.send_keys(file_path)

    hosted_path = driver.find_element(
        By.CSS_SELECTOR, 'tbody tr td:nth-child(3)')

    # Input default HTML with PATH
    html = driver.find_element(By.XPATH, "(//textarea)[2]")
    html_text = "<script> \n var frame = document.createElement('iframe');\n frame.style.border = '0'; \n frame.setAttribute('scrolling', 'no');\n var clickMacro = '${CLICK_URL}';\n var clickUrl = '';\n var click = clickMacro; \n if(clickUrl != '' && !clickMacro.includes(clickUrl)) {\n click = clickMacro+clickUrl;\n }\n var urlToBanner = '" + \
        hosted_path.text + \
        "'\n frame.src = urlToBanner + '?' + encodeURIComponent(click);\n window.document.body.appendChild(frame);\n </script> "
    html.send_keys(html_text)

    # Input default styling for iframe
    css = driver.find_element(By.XPATH, "(//textarea)[3]")
    css_text = "iframe{position: absolute;width: 100%;height: 100%;top: 0;left: 0;right: 0;bottom: 0;cursor: pointer;}"
    css.send_keys(css_text)

    # Click save and publish button
    save_btn.click()
    live_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@class='ml-6 v-btn v-btn--flat v-btn--icon v-btn--round theme--dark v-size--default primary--text'])[1]"))
    )
    # time.sleep(1)
    live_btn.click()

    # Time before hosting window shuts down
    time.sleep(120)
