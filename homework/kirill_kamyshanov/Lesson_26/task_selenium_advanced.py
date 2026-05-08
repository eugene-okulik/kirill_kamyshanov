import pytest
from selenium import webdriver

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def test_first(driver):
    driver.get("http://testshop.qa-practice.com/")
    wait = WebDriverWait(driver, 10)

    # Находим карточку товара и открываем её во второй вкладке
    customizable_desk = driver.find_element(By.CSS_SELECTOR, "[alt='Customizable Desk']")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(customizable_desk).key_up(Keys.CONTROL).perform()

    # Переключаемся на вторую вкладку
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    # Добавляем товар в корзину
    driver.find_element(By.XPATH, "//a[@id='add_to_cart']").click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="btn btn-secondary"]'))).click()

    # ждём пока добавление товара в корзину подгрузится
    wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-shopping-cart fa-stack"][1]')))

    # закрываем вторую вкладку и переключаемся на первую
    driver.close()
    driver.switch_to.window(tabs[0])

    # клик на корзину для проверки её содержимого
    wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="fa fa-shopping-cart fa-stack"][1]'))).click()

    # проверка содержимого корзины
    table_in_card = driver.find_element(By.LINK_TEXT, 'Customizable Desk (Steel, White)')
    assert table_in_card.is_displayed(), f"{table_in_card} is not displayed"


def test_second(driver):
    driver.get("http://testshop.qa-practice.com/")
    desk = driver.find_element(By.XPATH, "//img[@alt='Customizable Desk']")
    ActionChains(driver).move_to_element(desk).perform()
    driver.find_element(By.XPATH, '//a[@aria-label="Shopping cart"][1]').click()
    assert desk.is_displayed(), f"{desk} is not displayed"
