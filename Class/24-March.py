#to locate a frame there are three ways to using index name and as a web element
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)
driver.get("http://127.0.0.1:5500/page1.html")
driver.maximize_window()
actions=ActionChains(driver)
# driver.find_element(By.ID,"inp1").send_keys("SAUMYA")
# driver.switch_to.frame(0)
# sleep(2)
# driver.find_element(By.ID,"inp2").send_keys("RAHUL")
# sleep(2)
# driver.switch_to.frame(0)
# sleep(2)
# driver.find_element(By.ID,"inp3").send_keys("TANISH")

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
driver.find_element(By.ID,"inp1").send_keys("SAUMYA")
driver.switch_to.frame('frame1')
sleep(2)
driver.find_element(By.ID,"inp2").send_keys("RAHUL")
sleep(2)
driver.switch_to.frame('frame2')
sleep(2)
driver.find_element(By.ID,"inp3").send_keys("TANISH")







