from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(15)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@class='ico-register']").click()
driver.find_element(By.ID,"gender-male").click()
driver.find_element(By.ID,"FirstName").send_keys("Saumya")
driver.find_element(By.ID,"LastName").send_keys("Jain")
driver.find_element(By.ID,"Email").send_keys("saumya81@gmail.com")
driver.find_element(By.ID,"Password").send_keys("saumya1234")
driver.find_element(By.ID,"ConfirmPassword").send_keys("saumya1234")
driver.find_element(By.ID,"register-button").click()

