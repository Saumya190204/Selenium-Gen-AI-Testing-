from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)
# driver.get("https://www.google.com")
# driver.maximize_window()
#
# # print("the title is:",driver.title)
#
# expected='Google'
# actual=driver.title
# assert expected==actual,"Title mismatched"  #after comma in inverted commas we write the error that will be shown in case of an error as an error message
#
# driver.find_element(By.XPATH,"//textarea[@title='Search']").send_keys("Books")


#PRACTICE
driver.get("https://www.amazon.in")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()
expected='Amazon.in Bestsellers: The most popular items on Amazon'
actual=driver.title
assert expected==actual,"TITLE MISMATCHED"
driver.quit()