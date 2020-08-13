import time
from selenium.webdriver import Chrome
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec

@pytest.fixture()
def setpath():
        global driver
        #path = "C:\\chromedriver\\chromedriver.exe"
        driver = Chrome()
        yield
        driver.close()

def test_browser_open(setpath):
        driver.get("https:/www.theTestingWorld.com/testings")
        driver.maximize_window()
        driver.find_element_by_name("fld_username").send_keys("Preety")
        driver.find_element_by_name("fld_email").send_keys("preetygupta23@gmail.com")
        driver.find_element_by_name("fld_password").send_keys("abcd123")
        driver.find_element_by_xpath("//*[@name='fld_cpassword']").send_keys("abcd123")
        driver.find_element_by_name("phone").send_keys("8700546591")
        driver.find_element_by_name("address").send_keys("Gurgaon")
        driver.find_element_by_xpath("//input[@value='home']").click()
        obj = Select(driver.find_element_by_name("sex"))
        obj.select_by_index(2)


        obj = Select(driver.find_element_by_id("countryId"))
        obj.select_by_value("101")

        wait = WebDriverWait(driver,100)
        wait.until(ec.text_to_be_present_in_element((By.ID,"stateId"),"Haryana"))
        obj = Select(driver.find_element_by_id("stateId"))
        obj.select_by_visible_text("Haryana")

        wait = WebDriverWait(driver,100)
        wait.until(ec.text_to_be_present_in_element((By.ID,"cityId"),"Gurgaon"))
        obj = Select(driver.find_element_by_id("cityId"))
        obj.select_by_visible_text("Gurgaon")

        driver.find_element_by_name("zip").send_keys("122001")
        driver.find_element_by_name("terms").click()

        driver.get_screenshot_as_file("C:/Users/Preety/PycharmProjects/LearnPytest/ScreenShot1.png")
        driver.find_element_by_xpath("//input[@value='Sign up']").click()

        driver.execute_script("window.scrollTo(0,400);")

        driver.get_screenshot_as_file("C:/Users/Preety/PycharmProjects/LearnPytest/ScreenShot2.png")





