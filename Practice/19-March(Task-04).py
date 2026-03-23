from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(15)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
l1=[r"C:\Users\saumya\Downloads\HTML-CSS-JS(Gen-AI-Testing).txt",r"C:\Users\saumya\Downloads\PYTHON.txt"]
driver.find_element(By.ID,"singleFileInput").send_keys(r"C:\Users\saumya\Downloads\HTML-CSS-JS(Gen-AI-Testing).txt")
#driver.find_element(By.ID,"multipleFilesInput").send_keys(r"C:\Users\saumya\Downloads\HTML-CSS-JS(Gen-AI-Testing).txt").send_keys(r"C:\Users\saumya\Downloads\PYTHON.txt")
# for i in range(0,len(l1)):
#     driver.find_element(By.ID, "multipleFilesInput").send_keys(l1[i])

#THE OTHER WAY TO UPLOAD MULTIPLE FILES IN ONE GO
upload=driver.find_element(By.ID,"multipleFilesInput")
upload.send_keys(l1[0] + "\n" + l1[1])
driver.find_element(By.ID,"name").send_keys("saumya")
driver.find_element(By.ID,"email").send_keys("jain")
driver.find_element(By.ID,"phone").send_keys("1478523699")
driver.find_element(By.ID,"textarea").send_keys("")


