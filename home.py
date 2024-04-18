from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
time.sleep(2)
driver.execute_script("window.scrollBy(0, 600)")
driver.find_element_by_css_selector("div.woocommerce :nth-child(1) li.post-160").click()
driver.find_element_by_class_name("reviews_tab").click()
driver.find_element_by_class_name("star-5").click()
review=driver.find_element_by_id("comment")
review.send_keys("Nice book!")
name=driver.find_element_by_id("author")
name.send_keys("Mary")
email=driver.find_element_by_id("email")
email.send_keys("maria9459@gmail.com")
driver.find_element_by_id("submit").click()

driver.quit()