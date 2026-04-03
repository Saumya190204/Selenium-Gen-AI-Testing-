import pytest
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
o=ChromeOptions()
o.add_experimental_option("detach",True)
driver=Chrome(options=o)
@pytest.mark.parametrize("username,password",[("saumya","saum123"),("standard_user","secret_sauce")])
def test_log(username,password):
    driver.get("https://www.saucedemo.com")
    driver.maximize_window()
    driver.implicitly_wait(10)
    actual=password
    expected="secret_sauce"
    assert actual==expected
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.ID,"login-button").click()