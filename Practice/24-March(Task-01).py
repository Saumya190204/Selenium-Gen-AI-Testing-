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
driver.get("https://x.com/")
driver.maximize_window()
actions=ActionChains(driver)
ele=driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button']")
sleep(3)
driver.switch_to.frame(ele)
sleep(2)
driver.find_element(By.XPATH,"//div[@class='nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb oXtfBe-l4eHX']").click()

