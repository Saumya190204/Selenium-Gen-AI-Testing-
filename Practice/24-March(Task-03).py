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
driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(5)
actions=ActionChains(driver)
myntra=driver.find_element(By.XPATH,"//a[@href='https://www.myntra.com/']")
sleep(2)
cleartrip=driver.find_element(By.XPATH,"//a[@href='https://www.cleartrip.com/']")
sleep(2)
shopsy=driver.find_element(By.XPATH,"//a[@href='https://www.shopsy.in']")
sleep(2)



actions.scroll_to_element(myntra).perform()
sleep(1)
actions.click(myntra).perform()
sleep(1)
driver.switch_to.window(driver.window_handles[1])
print("The current url of myntra is :",driver.current_url)
print("The title of myntra is :",driver.title)
print("The current page id is :",driver.current_window_handle)
driver.close()
driver.switch_to.window(driver.window_handles[0])
# print(driver.current_url)


actions.scroll_to_element(cleartrip).perform()
sleep(1)
actions.click(cleartrip).perform()
sleep(1)
driver.switch_to.window(driver.window_handles[1])
sleep(5)
print("The current url of cleartrip is :",driver.current_url)
print("The title of cleartrip is :",driver.title)
print("The current page id is :",driver.current_window_handle)
driver.close()
driver.switch_to.window(driver.window_handles[0])


actions.scroll_to_element(shopsy).perform()
sleep(1)
actions.click(shopsy).perform()
sleep(1)
driver.switch_to.window(driver.window_handles[1])
print("The current url of shopsy is :",driver.current_url)
print("The title of shopsy is :",driver.title)
print("The current page id is :",driver.current_window_handle)
driver.close()
driver.switch_to.window(driver.window_handles[0])
