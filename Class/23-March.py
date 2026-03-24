# #KEYBOARD ACTIONS
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(10)
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# element=driver.find_element(By.ID,"twotabsearchtextbox")
# element.send_keys("Mobiles")
# #driver.find_element(By.ID,"nav-search-submit-button").click()
# element.send_keys(Keys.ENTER)
#
# from stringprep import b1_set
#
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(10)
# driver.get("https://demoqa.com/text-box")
# driver.maximize_window()
# element=driver.find_element(By.ID,"currentAddress")
# element.send_keys("JAIPUR,RAJASTHAN")
# element.send_keys(Keys.CONTROL,'A')
# element.send_keys(Keys.CONTROL,'C')
# el=driver.find_element(By.ID,"permanentAddress")
# el.send_keys(Keys.CONTROL,'V')
#ACTION CHAINS PERFORM TASK IN THREE STEPS
# 1.CREATE OBJECT
# 2.STORE ACTION
# 3.PERFORM
from idlelib.run import handle_tk_events

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




# driver.get("https://demoqa.com/buttons")
# driver.maximize_window()
# actions=ActionChains(driver)
# sleep(2)
# single_click=driver.find_element(By.XPATH,"//button[text()='Click Me']")
# actions.click(single_click).perform()
# double_click=driver.find_element(By.XPATH,"//button[text()='Double Click Me']")
# actions.double_click(double_click).perform()
# right_click=driver.find_element(By.XPATH,"//button[text()='Right Click Me']")
# actions.context_click(right_click).perform()




# driver.get("https://www.amazon.in")
# driver.maximize_window()
# el=driver.find_element(By.XPATH,"//img[@alt='VAYA HauteChef Cast Iron Kadai, 24 cm, Pre-Seasoned & Naturally Non-Stick, 100% Pure & Toxin-Free, Deep Design for...']")
# actions=ActionChains(driver)
# actions.scroll_to_element(el).perform()
# actions.click(el).perform()
#el=driver.find_element(By.XPATH,"//img[@alt='JBL Go 3 Wireless Portable Bluetooth Mini Speaker, Small Speaker with Pro Sound, Vibrant Colors with Rugged Fabric...']")
# actions.scroll_by_amount(0,2000).pause(3).perform()
# actions.scroll_from_origin()
# origin = ScrollOrigin.from_element(el)
# actions.scroll_from_origin(origin, 0, 1000).perform()
# origin = ScrollOrigin.from_viewport(0, 0)
# actions.scroll_from_origin(origin, 200, 1350).perform()
# el1=driver.find_element(By.XPATH,"(//div[@class='a-cardui _quad-multi-asin-card-v2_fluid_fluidCard__3hmFA'])[2]")
# actions.scroll_to_element(el1).perform()
# sleep(5)
# actions.click(el1).perform()

#MOVE TO ELEMENT :TO HOVER OVER AN ELEMENT
# el2=driver.find_element(By.XPATH,"//a[@href='https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0']")
# actions.move_to_element(el2).perform()



#CLICK AND HOLD ACTION
# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# driver.maximize_window()
# sleep(5)
# driver.find_element(By.XPATH,"//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
# sleep(5)
# driver.find_element(By.ID,"password").send_keys("SAUMYA123456")
# my=driver.find_element(By.XPATH,"//img[@src='assets/img/Revamp/icon_eye_close.svg']")
# actions=ActionChains(driver)
# actions.click_and_hold(my).pause(3).release().perform()


#DRAG AND DROP ELEMENT
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
# toDrag=driver.find_element(By.ID,"draggable")
# toDrop=driver.find_element(By.ID,"droppable")
# actions=ActionChains(driver)
# actions.pause(2).drag_and_drop(toDrag,toDrop).perform()


#_________________________________________________________________________________________________________
# TOPIC:WINDOW TABS HANDLING
# TO FETCH THE ADDRESS OF THE CURRENT WINDOW:current window handle
# TO FETCH THE ID OF ALL THE TABS:window.handler
# TO SWITCH WINDOW:switch.to.window()


driver.get("https://www.google.com")
sleep(1)
driver.maximize_window()
sleep(1)
actions=ActionChains(driver)
sleep(1)
# print(driver.current_window_handle)
# print(driver.title)
# print(driver.window_handles)
sleep(1)
driver.switch_to.new_window()
driver.get("https://www.amazon.in")
print(driver.current_window_handle)
print(driver.title)

print(driver.window_handles)
sleep(2)
driver.switch_to.window(driver.window_handles[0])

