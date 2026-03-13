#__________________________________________locator using class____________________________
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
# driver.find_element(By.CLASS_NAME,"nav-input.nav-progressive-attribute").send_keys("shirts")
# sleep(1)
# driver.find_element(By.ID,"nav-search-submit-button").click()

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.get("https://demoqa.com/text-box")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.TAG_NAME,"input").send_keys("Saumya Jain")
# driver.find_element(By.TAG_NAME,"input").send_keys("Saumya@21")
# sleep(2)
# driver.find_element(By.TAG_NAME,"textarea").send_keys("Jaipur")
# driver.find_element(By.TAG_NAME,"textarea").send_keys("Jajkjipur")

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.get("https://amazon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)



#____________________________________LINK_TEXT LOCATOR(IT WILL work for only anchor tags means that anchor tags is available with what data at display) PRACTICE-------------------------------------


# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.get("https://amazon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.LINK_TEXT,"Customer Service").click()


#_______________________________________________**IMPORTANT**__________________________________________


#ID,NAME,CLASSNAME,TAGNAME -these four are direct locators
#LINK TEXT,PARTIAL LINK TEXT:these two are text based locators
#CSS SELECTORS AND X-PATH SELECTORS:these two are expression based selectors

#------------------------------------------------------------------------------------------------------------------
#difference between link text and partial link text
#LINK_TEXT → Locates a hyperlink using the exact visible text of the link.
#PARTIAL_LINK_TEXT → Locates a hyperlink using only a part of the visible text of the link.
#These both are space sensitive and case-sensitive

#____________________PARTIAL LINK TEXT____________________________________________________________
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.get("https://amazon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.PARTIAL_LINK_TEXT,"Gam").click()

#__________________________ CSS SELECTORS______________________________________________________________
#syntax for locator in css selectors:tagname[attribute='value']\
#for eg<input id='link' type='text
#for verification:press ctrl+f in inspexct section and then types the  tagname[attribute='value'] and then press enter if the particular code get highlighjted and it shows 1 of 1



