from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.get("https://www.amazon.in")
sleep(2)
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT,"Mobiles").click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT,"XIAOMI 17 Ultra ").click()