import re
from typing import Literal
from test_UI_kkamyshanov_pw.pages.base_page import BasePage
from test_UI_kkamyshanov_pw.pages.locators import good_page_locators, common_locators
from test_UI_kkamyshanov_pw.pages.locators.common_locators import count_goods_in_card, change_currency_button, \
    change_to_eur_button
from playwright.sync_api import expect


class GoodPage(BasePage):

    def check_product_page_displayed(self):
        """Проверка отображения страницы товара"""

        price = self.find(good_page_locators.price_area_loc)
        expect(price, "Цена товара не отображается в '$' или '€'").to_have_text(re.compile(r"^\$.*|.*€$"))

        picture = self.find(good_page_locators.good_picture_loc)
        expect(picture, "Картинка товара не отображается").to_be_visible()

        add_to_cart_button = self.find(good_page_locators.add_to_cart_from_good_page_loc)
        expect(add_to_cart_button,
               "Кнопка добавления товара в корзину не отображается на странице товара").to_be_visible()

        add_one_button = self.find(common_locators.add_one_button_loc)
        expect(add_one_button, "Кнопка увеличения кол-ва товаров не отображается на странице товара").to_be_visible()

        remove_one_button = self.find(common_locators.remove_one_button_loc)
        expect(remove_one_button, "Кнопка уменьшения кол-ва товаров не отображается на странице товара").to_be_visible()

        add_qty_area = self.find(good_page_locators.add_qty_area_loc)
        expect(add_qty_area, "Зона добавления товара не отображается на странице товара").to_be_visible()

    def add_goods_in_card(self, count: int):
        """Добавление товара в корзину со страницы товара"""
        if not isinstance(count, int):
            raise TypeError("Ожидается числовой тип данных")
        if count < 0:
            raise ValueError("Ожидается число больше нуля")

        while count > 1:
            self.find(common_locators.add_one_button_loc).click()
            count -= 1

        add_button = self.find(good_page_locators.add_to_cart_from_good_page_loc)
        add_button.click()
        expect(self.find(count_goods_in_card)).not_to_be_empty()

    def assert_goods_was_added_in_card(self, expected_count: int):
        """Проверка добавления товара в корзину со страницы товара"""

        popup_text = self.find(good_page_locators.popup_title)
        expect(popup_text, "Попап с сообщением о добавлении товара не отобразился").to_be_visible()

        cart_icon = self.find(count_goods_in_card)
        (expect(cart_icon,
                f"Неправильное значение кол-ва товаров у иконки корзины: {cart_icon.inner_text()}, "
                f"ожидалось {expected_count}")
         .to_have_text(str(expected_count)))

    def change_currency_to_eur(self):
        """Изменить валюту на EUR. Не стал делать универсальной,
        т.к. после изменения валюты на евро пропадает кнопка изменения валюты"""

        self.find(change_currency_button).click()
        self.find(change_to_eur_button).click()

    def assert_price_displayed_in_currency(self, currency_sign: Literal["$", "€"]):
        """Здесь поведение системы специфическое: если цена товара в долларах, знак ставится в начале, если в евро -
        в конце. В реальном проекте уточнил зачем так сделано, а тут просто подстроился"""

        allowed = ["$", "€"]
        if currency_sign not in allowed:
            raise ValueError(f"Некорректная валюта. Допустимые: {allowed}")

        price = self.find(good_page_locators.price_area_loc)

        if currency_sign == "$":
            expect(price, f"Цена товара не в валюте'{currency_sign}'").to_have_text(re.compile(r'^$.*'))
        elif currency_sign == "€":
            expect(price, f"Цена товара не в валюте'{currency_sign}'").to_have_text(re.compile(r'.*€$'))
