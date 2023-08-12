from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
# Открытие сайта
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
acc_btn = driver.find_element_by_link_text("My Account")
acc_btn.click()
# Переход
email = driver.find_element_by_id("reg_email")
email.send_keys("Doter.222@yandex.ru")
passw = driver.find_element_by_id("reg_password")
passw.send_keys("!aS456789@")
reg_btn = driver.find_element_by_name("register")
reg_btn.click()
driver.quit()

