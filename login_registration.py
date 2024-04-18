from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(2)
driver.find_element_by_link_text("My Account").click()
username=driver.find_element_by_id("username")
username.send_keys("mary56784@gmail.com")
password=driver.find_element_by_id("password")
password.send_keys("adgjlqetuo1234")
driver.find_element_by_xpath("//input[@name='login']").click()
elements=driver.find_elements_by_partial_link_text("Logout")
if not elements:
    print("No element found")
else:
    element = elements[0]
driver.quit()