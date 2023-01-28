from selenium import webdriver

driver = webdriver.Chrome("c://chromedriver.exe")
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

driver.maximize_window()