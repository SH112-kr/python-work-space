from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("순천향대학교")
elem.send_keys(Keys.RETURN)
