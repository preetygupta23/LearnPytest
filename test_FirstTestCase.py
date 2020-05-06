from selenium.webdriver import Chrome
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
import Take_ScreenShot

def test_First():
    path = "C:\\chromedriver\\chromedriver.exe"
    driver: WebDriver = Chrome(executable_path=path)
    driver.get("https://www.theTestingWorld.com/testings")

    driver.maximize_window()
    Take_ScreenShot.take_ScreenShot(driver,"ScreenShot2")

#Sending text to textbox
    driver.find_element_by_name("fld_username").send_keys("hello")
    driver.find_element_by_name("fld_username").clear()
    driver.find_element_by_name("fld_username").send_keys("Preety")
    driver.find_element_by_name("fld_email").send_keys("preetygupta23@gmail.com")
    driver.find_element_by_xpath("//input[@name='fld_password']").send_keys("abcd123")
    driver.find_element_by_name("fld_cpassword").send_keys("abcd123")

    #Clicking on radio button
    driver.find_element_by_xpath("//input[@value='home']").click()


    Take_ScreenShot.take_ScreenShot(driver,"ScreenShot3")
    #selecting value from dropdown
    obj = Select(driver.find_element_by_name("sex"))
    obj.select_by_index(2)

    obj1= Select(driver.find_element_by_name("country"))
    obj1.select_by_value("101")
    driver.execute_script("window.scrollTo(0,400);")

   # obj2 = Select(driver.find_element_by_name("state"))
   # obj2.select_by_value("Haryana")

    #Click on checkbox
    driver.find_element_by_name("terms").click()
    #driver.find_element_by_link_text("X").click()

    #Click on link
    #driver.find_element_by_link_text("Read Detail").click()


    #driver.find_element_by_xpath("//input[@value='Sign up']").click()

    #driver.close()