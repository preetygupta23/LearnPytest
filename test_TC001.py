from selenium.webdriver import Chrome
import pytest

@pytest.mark.skip("duplicate")
def test_browser_open():
        path = "C:\\chromedriver\\chromedriver.exe"
        driver = Chrome(executable_path=path)
        driver.get("https:/www.theTestingWorld.com/testings")

@pytest.mark.skip("its duplicate")
def test_dup_browser_open():
        path = "C:\\chromedriver\\chromedriver.exe"
        driver = Chrome(executable_path=path)
        driver.get("https:/www.theTestingWorld.com/testings")
