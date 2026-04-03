import pytest
# browser = "firefox"



#example of skip with reason we can also avoid writing reason
# @pytest.mark.regression
# @pytest.mark.skip(reason="Feature not ready yet")
# def test_reg1():
#     assert 99>=29,"Not Greater Than"
#


#normal regression marker
# @pytest.mark.regression
# def test_reg2():
#     assert True==True,"Not True"



#example of skip if with reason and if condition we can skip writing reason
# @pytest.mark.regression
# @pytest.mark.skipif(browser == "firefox", reason="Not working in Firefox")
# def test_reg22():
#     assert True==True,"Noooot True"



#using parameterized
# @pytest.mark.parametrize("a,b",[(1,2),(2,3)])
# def test_add(a,b):
#     print(a+b)

# import pytest
# from selenium.webdriver import Chrome,ChromeOptions
# from selenium.webdriver.common.by import By
# from time import sleep
# o=ChromeOptions()
# o.add_experimental_option("detach",True)
# driver=Chrome(options=o)
# @pytest.mark.parametrize("username,password",[("saumya","saum123"),("standard_user","secret_sauce"),("problem_user","secret_sauce")])
# def test_log(username,password):
#     from selenium.webdriver import Chrome, ChromeOptions
#     from selenium.webdriver.common.by import By
#     from time import sleep
#     o = ChromeOptions()
#     o.add_experimental_option("detach", True)
#     driver = Chrome(options=o)
#     driver.get("https://www.saucedemo.com")
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     # actual=password
#     # expected="secret_sauce"
#     # assert actual==expected
#     driver.find_element(By.ID,"user-name").send_keys(username)
#     driver.find_element(By.ID,"password").send_keys(password)
#     driver.find_element(By.ID,"login-button").click()
#     assert "inventory" in driver.current_url



#-------------------------------------FIXTURE---------------------------------------

import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def driver():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)

    driver = Chrome(options=o)
    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


class TestLogin:

    def test_gender(self, driver):
        driver.find_element(By.ID, "gender-male").click()

    def test_firstname(self, driver):
        driver.find_element(By.ID, "FirstName").send_keys("Saumya")

    def test_lastname(self, driver):
        driver.find_element(By.ID, "LastName").send_keys("Jain")

    def test_email(self, driver):
        driver.find_element(By.ID, "Email").send_keys("saumya@gmail.com")

    def test_password(self, driver):
        driver.find_element(By.ID, "Password").send_keys("saumya@1234")

    def test_confirmpass(self, driver):
        driver.find_element(By.ID, "ConfirmPassword").send_keys("saumya@1234")

    def test_submit(self, driver):
        driver.find_element(By.ID, "register-button").click()