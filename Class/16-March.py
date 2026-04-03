#There are two types of traversing in xpath locator \
#1.Forward
#2.Backward
#for backward traversing there are three steps
#i.find the static element
# ii.from the static element find the common parent of static and dynamic element
# iii.fetch the dynamic element data
from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
driver=Chrome(options=o)
driver.get("https://demoqa.com/webtables")
sleep(2)
driver.maximize_window()
sleep(2)
salary=driver.find_element(By.XPATH,"//td[text()='Cierra']/..//td[5]")
print("Your Salary is ",salary.text)
department=driver.find_element(By.XPATH,"//td[text()='Vega']/..//td[6]")
print("Your Assigned Department is ",department.text)

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# #o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://the-internet.herokuapp.com/tables")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# due=driver.find_element(By.XPATH,"//td[text()='Tim']//following-sibling::td[2]")
# # sleep(4)
# print("The due amount is",due.text)


#In X-PATH there is concept of siblings to fetch the datat of dynmic element
# 1.following sibling
# 2.Preceding siblings
# the syntax for precefing sibling is :

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
#o.add_argument('--headless')#this is a chrome settings to not open browser everytime but everything is going in the background, and we can see the terminal result
# driver=Chrome(options=o)
# driver.get("https://www.amazon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("Mobiles")
# sleep(4)
# driver.find_element(By.ID,"nav-search-submit-button").click()
# sleep(4)
#price=driver.find_element(By.XPATH,"//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']/../../..//span[@class='a-price-whole']")
#print(price.text)
#driver.close()
# rate=driver.find_element(By.XPATH,"((//div[@class='a-section a-spacing-none puis-padding-right-small s-title-instructions-style puis-desktop-list-title-instructions-style'])[4]/..//div)[10]//span[@class='a-price']")
# print(rate.text)

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
rate=driver.find_element(By.XPATH,"(//div[@class='RG5Slk'])[5]/../..//div[@class='hZ3P6w DeU9vF']")
print(rate.text)
driver.close()