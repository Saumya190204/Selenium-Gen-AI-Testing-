# from time import sleep
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# driver.implicitly_wait(10)
# driver.get("https://demoqa.com/webtables")
# driver.maximize_window()
# driver.find_element(By.ID,"addNewRecordButton").click()
# driver.find_element(By.ID,"firstName").send_keys("Saumya")
# driver.find_element(By.ID,"lastName").send_keys("Jain")
# driver.find_element(By.ID,"userEmail").send_keys("saumya123@gmail.com")
# driver.find_element(By.ID,"age").send_keys("22")
# driver.find_element(By.ID,"salary").send_keys("50000")
# driver.find_element(By.ID,"department").send_keys("IT")
# driver.find_element(By.ID,"submit").click()
# name=driver.find_element(By.XPATH,"//td[text()='Saumya']").text
# salary=driver.find_element(By.XPATH,"//td[text()='Saumya']/..//td[5]").text
# print(name,":",salary)
# driver.close()


#USING WAITS
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)
driver.get("https://demoqa.com/webtables")
driver.maximize_window()
wait=WebDriverWait(driver,10)
btn=wait.until(EC.presence_of_element_located((By.ID,"addNewRecordButton")))
btn.click()
name=wait.until(EC.presence_of_element_located((By.ID,"firstName")))
name.send_keys("Saumya")
name=wait.until(EC.presence_of_element_located((By.ID,"lastName")))
name.send_keys("Jain")
name=wait.until(EC.presence_of_element_located((By.ID,"userEmail")))
name.send_keys("saumya1234@gmail.com")
name=wait.until(EC.presence_of_element_located((By.ID,"age")))
name.send_keys("22")
name=wait.until(EC.presence_of_element_located((By.ID,"salary")))
name.send_keys("50000")
name=wait.until(EC.presence_of_element_located((By.ID,"department")))
name.send_keys("IT")
btn1=wait.until(EC.presence_of_element_located((By.ID,"submit")))
btn1.click()
driver.close()

