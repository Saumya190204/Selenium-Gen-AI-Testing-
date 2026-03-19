# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(15)
# driver.get("https://www.google.com/")
# driver.maximize_window()
#driver.find_element(By.TAG_NAME,"a").click() #this is used to find the first anchor tag
# links=driver.find_elements(By.TAG_NAME,"a")
# for i in links:
#     print(i.text)
# print(links)
# print(len(links))
# lin=driver.find_elements(By.XPATH,"//a")
# for j in lin:
#     print(j.text)

# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(15)
# driver.get("https://www.google.com/")
# driver.maximize_window()
# element=driver.find_element(By.XPATH,"//a[@class='gb_A']")
# print(element.get_attribute("aria-label"))
# print(element.get_attribute("href"))


#NEW TASK
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(15)
driver.get("https://www.amazon.in/")
driver.maximize_window()
prod=driver.find_elements(By.XPATH,"//div[@class='nav-div']//a")
print(len(prod))
for i in range(len(prod)):
    element=prod[i]
    print(element.text,element.get_attribute("href"))