from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
# Открытие сайта
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
acc_btn = driver.find_element_by_link_text("My Account")
acc_btn.click()
# Переход
email = driver.find_element_by_id("username")
email.send_keys("Doter.222@yandex.ru")
passw = driver.find_element_by_id("password")
passw.send_keys("!aS456789@")
log_btn = driver.find_element_by_name("login")
log_btn.click()
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
android_btn = driver.find_element_by_css_selector("[alt='Android Quick Start Guide']")
android_btn.click()
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
book_new_price = driver.find_element_by_css_selector(".price > ins > span")
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
im_btn = driver.find_element_by_css_selector("[alt='Android Quick Start Guide']")
im_btn.click()
image = WebDriverWait(driver, 1).until(
    EC.invisibility_of_element((By.ID, "fullResImage")))
clo = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
close_btn = driver.find_element_by_class_name("pp_close")
close_btn.click()
driver.quit()
