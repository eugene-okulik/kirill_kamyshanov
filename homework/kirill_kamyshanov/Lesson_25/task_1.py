import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    return driver


def test_task_1(driver):
    target_field = ('xpath', '//input[@placeholder="Submit me"]')
    target_result = ('css selector', '.result-text')

    driver.get("https://www.qa-practice.com/elements/input/simple")
    text_field = driver.find_element(*target_field)
    text_field.send_keys("I_like_borsh")
    text_field.submit()
    actual_text = driver.find_element(*target_result).text
    print(actual_text)


# Задание 1
# Напишите программку, которая заходит на вот эту страницу: https://www.qa-practice.com/elements/input/simple,
# вводит какой-то текст в поле, делает submit , а после этого находит элемент,
# в котором отображается тот текст, который был введен и рапечатывает этот текст.
#
# Задание 2
# Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form и
# полностью заполнит форму (кроме загрузки файла) и нажмет Submit.
#
# Небольшая особенность
# Страничка эта немного кривая, иногда реклама перекрывает элементы и по ним невозможно кликнуть
# (но сейчас, смотрю, вообще реклама пропала). Если бы это было приложение, которое мы тестируем,
# это был бы баг. Но работаем с тем, что есть. И для нас это даже плюс, нужно найти как выкрутиться.
# Обойти это можно уменьшив размер экрана браузера - тогда элементы перераспределяются и становятся доступны.
# Но если реклама так и не появится, то ничего на странице не мешает.
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