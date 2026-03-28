from selenium.webdriver import Chrome,ChromeOptions
from time import sleep
from selenium.webdriver.common.by import By
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
driver.implicitly_wait(10)
import os
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
def testregister():
    el1=driver.find_element(By.XPATH,"//a[text()='Register']")
    el1.click()
def test_gender():
    gender=driver.find_element(By.ID,"gender-male")
    gender.click()
def test_fname():
    fname=driver.find_element(By.ID,"FirstName")
    fname.send_keys("Saumya")
def test_lname():
    lname=driver.find_element(By.ID,"LastName")
    lname.send_keys("Jain")
def test_email():
    mail=driver.find_element(By.ID,"Email")
    mail.send_keys("saumya1234@gmail.com")
def test_password():
    mail=driver.find_element(By.NAME,"Password")
    mail.send_keys("saumya1234")
def test_confirmpassword():
    mail=driver.find_element(By.NAME,"ConfirmPassword")
    mail.send_keys("saumya1234")
def test_regbtn():
    btn=driver.find_element(By.ID,"register-button")
    btn.click()