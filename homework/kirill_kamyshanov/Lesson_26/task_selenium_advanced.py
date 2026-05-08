import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver

@pytest.mark.skip
def test_first(driver):
    driver.get("http://testshop.qa-practice.com/")

    customizable_desk = driver.find_element(By.CSS_SELECTOR, "[alt='Customizable Desk']")
    # ActionChains(driver).click(button=2).perform()
    sleep(3)


# откройте первый (Customizable Desk) товар в новой вкладке
# Перейдите на вкладку с товаром
# Добавьте товар в корзину
# Нажмите на кнопку Add to Cart
# В открывшемся попапе нажмите Continue shopping
# Закройте вкладку с товаром
# На начальной вкладке откройте корзину
# Убедитесь, что в корзине тот товар, который вы добавляли















def test_second(driver):
    driver.get("http://testshop.qa-practice.com/")
    desk = driver.find_element(By.XPATH, "//img[@alt='Customizable Desk']")
    ActionChains(driver).move_to_element(desk).perform()
    driver.find_element(By.XPATH, '//a[@aria-label="Shopping cart"][1]').click()
    assert desk.is_displayed()


