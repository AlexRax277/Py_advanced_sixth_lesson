from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('https://passport.yandex.ru/auth/')
elem = driver.find_element_by_name('login')
time.sleep(2)
elem.send_keys('rakovchen.alexander@ya.ru')
time.sleep(2)
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem_2 = driver.find_element_by_name('passwd')
time.sleep(2)
elem_2.send_keys('2772126021rocky')
time.sleep(2)
elem_2.send_keys(Keys.RETURN)
time.sleep(5)
assert 'No results found.' not in driver.page_source
driver.close()
driver.quit()
