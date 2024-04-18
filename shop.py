from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.get("https://practice.automationtesting.in/")
time.sleep(2)

driver.find_element_by_id("menu-item-40").click()

driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_css_selector("ul.products :nth-child(4) a.button").click()
time.sleep(5)

driver.find_element_by_css_selector("a.wpmenucart-contents").click()

proceed = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, "a.checkout-button")) )
driver.find_element_by_css_selector("a.checkout-button").click()

firstname = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "billing_first_name")))
firstname.send_keys("Mary")

lastname = driver.find_element_by_id("billing_last_name")
lastname.send_keys("Ivanova")

phone = driver.find_element_by_id("billing_phone")
phone.send_keys("89990000000")

driver.find_element_by_id("select2-chosen-1").click()
country=driver.find_element_by_id("s2id_autogen1_search")
country.send_keys("Russia")
driver.find_element_by_class_name("select2-match").click()

address=driver.find_element_by_id("billing_address_1")
address.send_keys("Asdfg")

town=driver.find_element_by_id("billing_city")
town.send_keys("Moscow")

state=driver.find_element_by_id("billing_state")
state.send_keys("Russia")

postcode=driver.find_element_by_id("billing_postcode")
postcode.send_keys("123456")

driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
pay = driver.find_element_by_css_selector("[value='cheque']")
pay.click()

driver.find_element_by_id("place_order").click()

element=WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))

element2=WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot :nth-child(3) td"), "Direct Bank Transfer"))

driver.quit()
