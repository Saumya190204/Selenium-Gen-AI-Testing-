from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://www.flipkart.com/")
sleep(5)
driver.maximize_window()
sleep(5)
driver.find_element(By.CLASS_NAME,"nw1UBF.v1zwn25").send_keys("mobiles")
sleep(2)
driver.find_element(By.CLASS_NAME,"XFwMiH").click()
sleep(2)
driver.find_element(By.XPATH,"//div[@class='RG5Slk']")
sleep(2)
rate=driver.find_element(By.XPATH,"(//div[@class='RG5Slk'])[4]/../..//div[@class='hZ3P6w DeU9vF']")
print(rate.text)
driver.close()