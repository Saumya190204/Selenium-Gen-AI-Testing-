# from asyncio import timeout
# from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By  #keys supportchains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)
driver.get("https://www.flipkart.com/")
driver.implicitly_wait(10)
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
driver.maximize_window()
wait=WebDriverWait(driver,10)
text=wait.until(EC.presence_of_element_located((By.XPATH,"//input[@class='nw1UBF v1zwn25']")))
text.send_keys('Mobiles')
press=wait.until(EC.presence_of_element_located((By.XPATH,"//button[@class='XFwMiH']")))
press.click()
name=wait.until(EC.presence_of_element_located((By.XPATH,"(//div[@class='RG5Slk'])[15]")))
print(name.text)
driver.close()