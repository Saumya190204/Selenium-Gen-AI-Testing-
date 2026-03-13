from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.facebook.com")
sleep(2)
driver.maximize_window()
sleep(2)
driver.find_element(By.NAME,"email").send_keys("saumya190204@gmail.com")
driver.find_element(By.NAME,"pass").send_keys("saumya1234")