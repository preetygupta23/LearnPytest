from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_KeyBoard():
    path = "C:\\chromedriver\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.theTestingWorld.com/testings")

    driver.maximize_window()

    #Sending text to textbox
    driver.find_element_by_name("fld_username").send_keys("hello")

    act=ActionChains(driver)
    #act.send_keys(Keys.CONTROL).send_keys("a").perform()   # Its not working.
    act.send_keys(Keys.TAB).perform()


