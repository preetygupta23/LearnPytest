from selenium.webdriver import Chrome
import pytest
import time

@pytest.fixture()
def setpath():
        global driver
        path = "C:\\chromedriver\\chromedriver.exe"
        driver = Chrome(executable_path=path)
        driver.get("https:/www.theTestingWorld.com/testings")
        driver.maximize_window()
        yield
        driver.close()

def test_browser_open(setpath):
        time.sleep(10)
        driver.find_element_by_xpath("//Label[text()='Login']").click()
        driver.find_element_by_name("_txtUserName").send_keys("test")
        driver.find_element_by_name("_txtPassword").send_keys("test")
        driver.find_element_by_xpath("//input[@type='submit' and @value ='Login']").click()
        driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//a[contains(text(),'Update')]").click()
        allWindows= driver.window_handles
        print(allWindows)

        for win in allWindows:
                driver.switch_to.window(win)
                if(driver.current_url=='https://www.thetestingworld.com/testings/manage_customer.php'):
                        driver.find_element_by_xpath("//button[text()='Start Download']").click()
                        time.sleep(10)
                        driver.close()


        driver.switch_to.window(allWindows[0])
        print(driver.current_url)

