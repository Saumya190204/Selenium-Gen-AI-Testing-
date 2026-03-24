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
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Log in']").click()
el=driver.find_element(By.XPATH,"//iframe[@id='auth-login-ui']")
driver.switch_to.frame(el)
el2=driver.find_element(By.XPATH,"//iframe[@title='Sign in with Google Button']")
driver.switch_to.frame(el2)
driver.find_element(By.XPATH,"//div[@class='nsm7Bb-HzV7m-LgbsSe-bN97Pc-sM5MNb oXtfBe-l4eHX']").click()