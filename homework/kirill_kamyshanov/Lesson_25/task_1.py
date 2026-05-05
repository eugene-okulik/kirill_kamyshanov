import time
import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    return driver

@pytest.mark.skip()
def test_task_1(driver):
    target_field = ('xpath', '//input[@placeholder="Submit me"]')
    target_result = ('css selector', '.result-text')

    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_field = driver.find_element(*target_field)
    text_field.send_keys("I_like_borsh")
    text_field.submit()
    actual_text = driver.find_element(*target_result).text
    print(actual_text)



def test_task_2(driver):
    submit = ('css selector', 'button[type="submit"]')

    driver.get('https://demoqa.com/automation-practice-form')

    driver.find_element(By.CSS_SELECTOR, '#firstName').send_keys("Вова")
    driver.find_element(By.CSS_SELECTOR, '#lastName').send_keys("Рябченко")
    driver.find_element(By.CSS_SELECTOR, '#userEmail').send_keys("example@gmail.com")
    driver.find_element(By.XPATH, '//input[@value="Male"]').click()
    driver.find_element(By.CSS_SELECTOR, '[id="userNumber"]').send_keys('79999999999')
    driver.find_element(By.XPATH, '//input[@class="subjects-auto-complete__input"]').send_keys('some_text')
    driver.find_element(By.CSS_SELECTOR, '#hobbies-checkbox-2').click()
    driver.find_element(By.XPATH, '//*[@placeholder="Current Address"]').send_keys('Kazan')




    subject_field = driver.find_element(By.XPATH, '//input[@class="subjects-auto-complete__input"]')
    subject_field.send_keys('some_text')
    time.sleep(4)




    # submit_button = driver.find_element(*submit)
    #
    # # 1. прокрутить
    # driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    #
    # # 2. дождаться кликабельности (после прокрутки)
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    # # time.sleep(1)
    # # 3. кликнуть
    # driver.execute_script("arguments[0].click();", submit_button)


    # title = driver.find_element('xpath', '//div[@class="modal-title h4"]')
    # print(title.text)
    # sent_data = driver.find_elements(By.CSS_SELECTOR, 'td')
    # for sent in sent_data:
    #     print(sent.text)
    # print(sent_data[0].text) # 1-й
    # print(sent_data[-1].text) # посл-й



# Задание 2
# Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form
# и полностью заполнит форму (кроме загрузки файла) и нажмет Submit.
#
#
# После отправки вам будет отображено окошко с тем что вы ввели.
# Получите со страницы содержимое этого окошка и распечатайте (выведите на экран).

# Задание 3
# Часть 1
# Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/select/single_select,
# выбирает какой-нибудь вариант из Choose language, кликает Submit и проверяет,
# что в окошке с результатом отображается тот вариант, который был выбран.
#
# Часть 2
# Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2,
# нажмет Start, и проверит, что на странице появляется текст "Hello World!"