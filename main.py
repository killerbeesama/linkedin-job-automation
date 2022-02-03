import time
from numpy import sign
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

EMAIL = "<your email>"
PASSWORD = "<your password>"

driver_path = "<your driver path>"
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("your linkedin url")
##------sign in-------##
sign_in = driver.find_element_by_css_selector("div .nav__button-secondary")
sign_in.click() 

##------fill up------##
time.sleep(3)
email = driver.find_element_by_name("session_key")
email.send_keys(EMAIL)
password = driver.find_element_by_name("session_password")
password.send_keys(PASSWORD)
signin = driver.find_element_by_css_selector(".login__form_action_container button")
signin.click()

driver.quit()