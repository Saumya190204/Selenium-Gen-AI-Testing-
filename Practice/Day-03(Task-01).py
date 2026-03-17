from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless')
driver=Chrome(options=o)
driver.get("https://www.amazon.in")
sleep(2)
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")
sleep(4)
driver.find_element(By.ID,"nav-search-submit-button").click()
sleep(2)
price=driver.find_element(By.XPATH,"//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']/../../..//span[@class='a-price-whole']")
print(price.text)
driver.close()