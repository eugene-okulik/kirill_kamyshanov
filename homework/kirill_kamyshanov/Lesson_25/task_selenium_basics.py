import pytest
import random
from faker import Faker
from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def test_task_1(driver):
    test_text = "I_like_borsh"

    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_field = driver.find_element(By.XPATH, '//input[@placeholder="Submit me"]')
    text_field.send_keys(test_text)
    text_field.submit()
    actual_text = driver.find_element(By.CSS_SELECTOR, '.result-text').text
    print(actual_text)
    assert actual_text == test_text, f"Ожидался текст {test_text}, но получен {actual_text}"


def test_task_2(driver):
    wait = WebDriverWait(driver, 20)
    fake = Faker()

    driver.get('https://demoqa.com/automation-practice-form')
    driver.execute_script("window.scrollBy(0, 250);")
    driver.find_element(By.CSS_SELECTOR, '#firstName').send_keys(fake.first_name())
    driver.find_element(By.CSS_SELECTOR, '#lastName').send_keys(fake.last_name())
    driver.find_element(By.CSS_SELECTOR, '#userEmail').send_keys(fake.email())
    driver.find_element(By.XPATH, '//input[@value="Male"]').click()
    driver.find_element(By.CSS_SELECTOR, '[id="userNumber"]').send_keys(random.randint(79000000000, 79999999999))
    driver.find_element(By.CSS_SELECTOR, '#hobbies-checkbox-2').click()
    driver.find_element(By.XPATH, '//*[@placeholder="Current Address"]').send_keys(fake.address())

    subjects_button = driver.find_element(By.XPATH, '//input[@class="subjects-auto-complete__input"]')
    subjects_button.click()
    subjects_button.send_keys("English")
    subjects_button.send_keys(Keys.ENTER)

    wait.until(EC.presence_of_element_located((By.ID, 'submit'))).click()

    response_table = driver.find_element(By.CSS_SELECTOR, '.table-responsive')
    print(response_table.text)


def test_task_3_1(driver):
    language = 'Java'
    driver.get("https://www.qa-practice.com/elements/select/single_select")

    select = driver.find_element(By.ID, 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_visible_text(language)

    submit_button = driver.find_element(By.CSS_SELECTOR, '[name="submit"]')
    submit_button.click()

    result_field = driver.find_element(By.ID, 'result-text')
    assert result_field.text == language, f"Ожидался текст {language}, но получен {result_field.text}"


def test_task_3_2(driver):
    expected_text = "Hello World!"
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    driver.find_element(By.XPATH, "//button").click()
    result_area = driver.find_element(By.XPATH, "//h4[text()='Hello World!']")
    assert result_area.text == expected_text, f"Ожидался текст {expected_text}, но получен {result_area.text}"
