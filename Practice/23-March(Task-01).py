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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
actions=ActionChains(driver)
el1=driver.find_element(By.XPATH,"//button[text()='Copy Text']")
actions.double_click(el1).perform()
btn=driver.find_element(By.XPATH,"//button[text()='START']")
actions.click(btn).perform()
btn2=driver.find_element(By.XPATH,"//button[text()='Point Me']")
actions.move_to_element(btn2).pause(2).perform()
drag=driver.find_element(By.XPATH,"//div[@id='draggable']")
drop=driver.find_element(By.XPATH,"//div[@id='droppable']")
actions.drag_and_drop(drag,drop).perform()



