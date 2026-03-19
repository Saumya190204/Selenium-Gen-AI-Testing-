from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(15)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']").send_keys('watch')
driver.find_element(By.ID,"nav-search-submit-button").click()
# im=driver.find_elements(By.XPATH,"//img")
# print(len(im))
im1=driver.find_elements(By.XPATH,"//img[@class='s-image']")
print(len(im1))
im1[5].click()  #to click a particular element among the list of all elements

