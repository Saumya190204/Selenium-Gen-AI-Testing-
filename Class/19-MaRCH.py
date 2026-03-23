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
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(15)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# prod=driver.find_elements(By.XPATH,"//div[@class='nav-div']//a")
# print(len(prod))
# for i in range(len(prod)):
#     element=prod[i]
#     print(element.text,element.get_attribute("href"))




#is displayed, is enabled,is selected
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(15)
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# login=driver.find_element(By.XPATH,"(//span[@class='x1lliihq x193iq5w x6ikm8r x10wlt62 xlyipyv xuxw1ft'])[1]")
# print("displayed :",login.is_displayed())
# print("enabled :",login.is_enabled())
# print("selected :",login.is_selected())
# sub=driver.find_element(By.XPATH,"//input[@type='submit']")
# print("displayed :",sub.is_displayed())
# print("enabled :",sub.is_enabled())
# print("selected :",sub.is_selected())



# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(15)
# driver.get("https://www.naukri.com/")
# driver.maximize_window()
# driver.find_element(By.ID,"register_Layer").click()
# btn=driver.find_element(By.XPATH,"//button[@class='submitbtn resman-btn-primary resman-btn-regular resman-btn-disabled']")
# print("Display",btn.is_displayed())
# print("enabled",btn.is_enabled())

# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(15)
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
# cb=driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
# print("selected : ",cb.is_selected())
# cb2=driver.find_element(By.XPATH,"//input[@type='checkbox'][2]")
# print("selected : ",cb2.is_selected())
# driver.find_element(By.XPATH,"//input[@type='checkbox'][1]").click()
# cb=driver.find_element(By.XPATH,"//input[@type='checkbox'][1]")
# print("selected : ",cb.is_selected())


#WORKING ON FORMS IN Selenium
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(15)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.find_element(By.ID,"firstName").send_keys("Saumya")
driver.find_element(By.ID,"lastName").send_keys("Jain")
driver.find_element(By.ID,"userEmail").send_keys("saumya19@gmail.com")
driver.find_element(By.ID,"gender-radio-1").click()
# driver.find_element(By.XPATH,"//div[@class='subjects-auto-complete__input-container css-19bb58m']").send_keys("Hindi")
# driver.find_element(By.XPATH,"//div[@class='subjects-auto-complete__input-container css-19bb58m']").send_keys(',English')
driver.find_element(By.ID,"userNumber").send_keys("98745633100")
driver.find_element(By.ID,"dateOfBirthInput").click()
driver.find_element(By.XPATH,"(//div[@class='react-datepicker__week'][3]//div)[3]").click()
driver.find_element(By.ID)
