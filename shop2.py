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
driver.execute_script("window.scrollBy(0, 300);")
# Переход
shop_btn = driver.find_element_by_id("menu-item-40")
shop_btn.click()
add_btn = driver.find_element_by_css_selector("[data-product_id='182']")
add_btn.click()
time.sleep(5)
cart_btn = driver.find_element_by_class_name("cartcontents")
cart_btn.click()
time.sleep(5)
