# we use two :find_element(locator_name,locator_value)-this is for single elements..this return a single web element
#If the element does not exist, Selenium throws an error(No such Element exception
# 2.find_elements(locator_name,locator_value):multiple element...this return list of web elements.If the element does not exist, Selenium throws an error.this will return an empty list

#Locators:locators are of 8 types:
# i.ID
# ii.Name
# iii.CLASSNAME
# IV.TAG
# V.LINK TEXT+
# VI.PARTIAL LINK TEXT
# VII.CSS SELECTORS
# VIII.XPATH

#-------------------------------ENTER VALUES IN DEMOQA AND SUBMIT----------------------------


# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.ID,'userName').send_keys("Saumya Jain")
# sleep(2)
# driver.find_element(By.ID,'userEmail').send_keys("saumya190204@gmail.com")
# sleep(2)
# driver.find_element(By.ID,'currentAddress').send_keys("Malviya Nagar Jaipur")
# sleep(2)
# driver.find_element(By.ID,'permanentAddress').send_keys("Malviya Nagar Jaipur")
# sleep(2)
# driver.find_element(By.ID,'submit').click()
# sleep(2)


#-------------------------SEARCH SOMETHING IN AMAZON INPUT FIELD
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
#
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.ID,"twotabsearchtextbox").send_keys("shoes")
# sleep(2)
# driver.find_element(By.ID,"nav-search-submit-button").click()



