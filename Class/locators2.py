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
# driver.find_element(By.TAG_NAME,"textarea").send_keys("Jaipur")

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


#ID,NAME,CLASS NAME,TAG NAME -these four are direct locators
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
#syntax for locator in CSS selectors:tag name[attribute='value']\
#for eg<input id='link' type='text
#for verification:press ctrl+f in inspect section and then types the  tag name[attribute='value'] and then press enter if the particular code get highlighted, and it shows 1 of 1

#--------------------SHORTCUT FOR ID CSS SELECTOR ---------------------------------
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
# driver.find_element(By.CSS_SELECTOR,"userName").send_keys("Saumya")

#__________________________________________________________LOCATOR-XPATH-------------------------------------------------
# IT USE XML-user defined pathlib
# XML path......we can travel forward or backward using XML path
# we can locate elements based on text as well as attribute
# used for dynamic elements
#there are two types of xpath :Absolute path:/,starts from root
# and Relative path://,directly jump to the element

#XPath using Attribute
#Syntax
#//tag[@attribute='value']

#-------------------------------------------code for x path--------------------------------------------------
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


#1.XPath using Attribute
#Syntax
#//tag[@attribute='value']


# driver.find_element(By.XPATH,"//input[@placeholder='Full Name']").send_keys("Saumya")
# sleep(2)
# driver.find_element(By.XPATH,"//button[@id='submit']").click()


#2.XPath using Attribute
#Syntax
#//tag name[text()='value']
#value will include the visible text
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.get("https://www.amazon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)
#driver.find_element(By.XPATH,"//span[text()='Refrigerators']").click()

#NOW INSTEAD OF WRITING text() function we can use "."
#there is an advantage of using . instead of using text() as that element can access through its parent element also
#driver.find_element(By.XPATH,"//span[.='Refrigerators']").click()  #this is the example os using "." and accessing the element using the exact particular element
#driver.find_element(By.XPATH,"//div[text()='Figurines, vases & more']").click() #this is the example of using "." and accessing the element using its parent element

#_____________________________________________________________________________________________________
#XPath using contains() with Attribute
# Syntax
#  //tagname[contains(@attribute,'value')]
#Meaning:
# Find an element
# whose attribute contains a specific partial value

# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.get("https://www.amazon.in")
# sleep(2)
# driver.maximize_window()
# sleep(2)
#driver.find_element(By.XPATH,"//a[contains(@href,'/gp/bestsellers/?ref_=nav_cs_bests')]").click()
#driver.find_element(By.XPATH,"//a[contains(text(),'Bestseller')]").click()
#driver.find_element(By.XPATH,"(//a[contains(@class,'nav-a')])[14]").click()



#WHENEVER WE WISH TO LOCATE ELEMENT BASED ON STRUCTURE.ATTRIBUTE OR TEXT WE CAN USE XPATH
#IN THE X PATH LOCATOR THE INDEXING STARTS FROM 1 NOT FROM 0
