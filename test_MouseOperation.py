from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_First():
    path = "C:\\chromedriver\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("https://www.theTestingWorld.com")



    act = ActionChains(driver)
    #act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()
    #act.context_click().perform()
    #driver.find_element_by_xpath("//span[@class='menu-title']")
    act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'VIDEOS')]")).perform()