#to locate a frame there are three ways to using index name and as a web element
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(10)
# driver.get("http://127.0.0.1:5500/page1.html")
# driver.maximize_window()
# actions=ActionChains(driver)
# driver.find_element(By.ID,"inp1").send_keys("SAUMYA")
# driver.switch_to.frame(0)
# sleep(2)
# driver.find_element(By.ID,"inp2").send_keys("RAHUL")
# sleep(2)
# driver.switch_to.frame(0)
# sleep(2)
# driver.find_element(By.ID,"inp3").send_keys("TANISH")
# driver.switch_to.parent_frame()
# driver.find_element(By.ID,"inp2").send_keys("MANAS")
# driver.switch_to.parent_frame()
# driver.find_element(By.ID,"inp1").send_keys("SAUMY JAINA")
# driver.switch_to.default_content()
# driver.find_element(By.ID,"inp1").send_keys("SAUMY JAINA")


#OTHER WAY TO SWITCHING TO GFRAME USING FRAME ID

# driver.find_element(By.ID,"inp1").send_keys("SAUMYA")
# driver.switch_to.frame('frame1')
# sleep(2)
# driver.find_element(By.ID,"inp2").send_keys("RAHUL")
# sleep(2)
# driver.switch_to.frame('frame2')
# sleep(2)
# driver.find_element(By.ID,"inp3").send_keys("TANISH")

#OTHER WAY TO ACCESS INPUT PLACEHOILDER USING NAME

# driver.find_element(By.NAME,"box1").send_keys("SAUMYA")
# driver.switch_to.frame('frame1')
# sleep(2)
# driver.find_element(By.NAME,"box2").send_keys("RAHUL")
# sleep(2)
# driver.switch_to.frame('frame2')
# sleep(2)
# driver.find_element(By.NAME,"box3").send_keys("TANISH")


#TO ACCESS ANY WEB ELEMENT 
# driver.find_element(By.ID,"inp1").send_keys("SAUMYA")
# driver.switch_to.frame('frame1')
# sleep(2)
# driver.find_element(By.ID,"inp2").send_keys("RAHUL")
# sleep(2)
# driver.switch_to.frame('frame2')
# sleep(2)
# driver.find_element(By.ID,"inp3").send_keys("TANISH")


#HANDLING ALERTS AND POP-UP's
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#FIRST TYPE OF ALERT-SIMPLE ALERT

# driver.find_element(By.ID,"alertBtn").click()
# alert=driver.switch_to.alert
# sleep(2)
# alert.accept()

#SECOND TYPE OF ALERT-CONFIRMATION ALERT
# driver.find_element(By.ID,"confirmBtn").click()
# alert=driver.switch_to.alert
# sleep(2)
# alert.accept()
#alert.dismiss()

#SECOND TYPE OF ALERT-PROMPT ALERT
# driver.find_element(By.ID,"promptBtn").click()
# alert=driver.switch_to.alert
# sleep(2)
# alert.send_keys("SAUMYA JAIN")
# alert.accept()


# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# o.add_experimental_option("prefs", {"safebrowsing.enabled": True})
# driver=Chrome(options=o)
# driver.implicitly_wait(10)
# driver.get("https://www.python.org/downloads/")
# driver.maximize_window()
# sleep(2)
# el=driver.find_element(By.XPATH,"(//a[text()='Python 3.14.3'])[4]")
# sleep(2)
# el.click()


#UPLOAD AND DOWNLOAD
# from selenium.webdriver import Chrome,ChromeOptions
# from time import sleep
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# o.add_experimental_option("prefs", {"safebrowsing.enabled": True}) #Run Chrome with safe browsing security enabled.”
# o.add_argument("--disable-notifications")  #Start Chrome with notifications turned OFF.”
# driver=Chrome(options=o)
# driver.implicitly_wait(10)
# driver.get("https://www.easemytrip.com/flights.html?utm_campaign=788997081&utm_source=g_c&utm_medium=cpc&utm_term=e_easemytrip&adgroupid=39319940377&gad_source=1&gad_campaignid=788997081&gbraid=0AAAAADo_0-h3QJ-p11y-Kv-NZh2sT2JIk&gclid=Cj0KCQjw7IjOBhDyARIsAFzrWQzArh3b4LZuM2Ju0hD0jxLkAiktF-EhQVubttYblc6zTMfkxsmVHIQaAlmWEALw_wcB")
# driver.maximize_window()
# sleep(2)




from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
o.add_argument("--disable-notifications")
driver=Chrome(options=o)
driver.implicitly_wait(10)
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//input[@class='ng-tns-c69-9 ui-inputtext ui-widget ui-state-default ui-corner-all ng-star-inserted']").click()
# sleep(2)
# driver.find_element(By.XPATH,"//span[@class='ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9']").click()
# driver.find_element(By.XPATH,"//span[@class='ui-datepicker-next-icon pi pi-chevron-right ng-tns-c69-9']").click()
# sleep(2)
# driver.find_element(By.XPATH,"(//a[@class='ui-state-default ng-tns-c69-9 ng-star-inserted'])[24]").click()
# sleep(2)
