from selenium.webdriver import Chrome

def test_WindowHandler():
   path = "C:\\chromedriver\\chromedriver.exe"
   driver = Chrome(executable_path=path)
   driver.get("https:/www.naukri.com")

   driver.implicitly_wait(300)

   driver.maximize_window()

   AllWindow = driver.window_handles

   for win in AllWindow:
     driver.switch_to.window(win)
     if driver.current_url=="https:/www.naukri.com":
        print("this is the main window")
     else:
        driver.close()