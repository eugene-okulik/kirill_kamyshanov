import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# element = '//div[@id="lunaradiobuttonvibe"]'
# element = ('xpath', '//div[@id="lunaradiobuttonvibe"]')
url = 'https://lofiradio.ru/'
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(url)
time.sleep(3)

# driver.find_element(By.ID, 'lunaradiobuttonvibe').click()
# driver.find_element(By.XPATH, '//div[@id="lunaradiobuttonvibe"]').click()
element = ('xpath', '//div[@id="lunaradiobuttonvibe"]')
driver.find_element(*element).click()
time.sleep(3)


