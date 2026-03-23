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
driver.get("https://www.nike.in/")
driver.maximize_window()
actions=ActionChains(driver)
kid=driver.find_element(By.XPATH,"//span[text()='Kids']")
actions.move_to_element(kid).perform()
sleep(2)
actions.click(kid).perform()
sleep(4)
# print(driver.current_url)
driver.switch_to.window(driver.window_handles[1])
sleep(2)
# print(driver.current_url)
shop=driver.find_element(By.XPATH,"//a[@href='/elevate-their-style/c/94039']")
actions.click(shop).perform()
sho=driver.find_element(By.XPATH,"//img[@src='https://adn-static1.nykaa.com/nykdesignstudio-images/pub/media/catalog/product/d/0/d08605bNike-IM6641-400_1.jpg?rnd=20200526195200&tr=w-512']")
sleep(2)
actions.scroll_to_element(sho).perform()
sleep(2)
actions.click(sho).perform()
sleep(2)
driver.switch_to.window(driver.window_handles[2])
sleep(2)
driver.find_element(By.XPATH,"//label[@for='grid-selector-input-NIKEX00023805']").click()
sleep(2)
driver.find_element(By.XPATH,"//button[text()='Add to Bag']").click()