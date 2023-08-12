from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
# Открытие сайта
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
# Переход
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
add_btn = driver.find_element_by_css_selector("[data-product_id='182']")
add_btn.click()
time.sleep(5)
cart_btn = driver.find_element_by_class_name("cartcontents")
cart_btn.click()
time.sleep(5)
but = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.alt.wc-forward")))
proceed_btn = driver.find_element_by_class_name("checkout-button.button.alt.wc-forward")
proceed_btn.click()
name = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")))
first = driver.find_element_by_id("billing_first_name")
first.send_keys("Andrew")
last = driver.find_element_by_id("billing_last_name")
last.send_keys("Buda")
email = driver.find_element_by_id("billing_email")
email.send_keys("Doter.222@yandex.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("8954231561")
sel_btn = driver.find_element_by_class_name("select2-arrow")
sel_btn.click()
search = driver.find_element_by_id("s2id_autogen1_search")
search.send_keys("Russia")
rus_btn = driver.find_element_by_class_name("select2-match")
rus_btn.click()
address = driver.find_element_by_css_selector("p > #billing_address_1")
address.send_keys("Gorodododdododo")
town = driver.find_element_by_css_selector("p > #billing_city")
town.send_keys("New York")
state = driver.find_element_by_css_selector("p > #billing_state")
state.send_keys("Brolan")
codee = driver.find_element_by_css_selector("p > #billing_postcode")
codee.send_keys("329012")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
cheque_btn = driver.find_element_by_css_selector("[value='cheque']")
cheque_btn.click()
order_btn = driver.find_element_by_id("place_order")
order_btn.click()
thank = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
cheque1 = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) > td"), "Check Payments"))
driver.quit()
