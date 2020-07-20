from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.maximize_window()
time.sleep(2)
driver.get("https://www.baidu.com")
time.sleep(2)
driver.find_element_by_id('kw').send_keys('python')
time.sleep(2)
driver.find_element_by_id('su').click()
time.sleep(2)
driver.quit()
