import re
from typing import Literal

from test_UI_kkamyshanov_pw.pages.base_page import BasePage
from test_UI_kkamyshanov_pw.pages.locators import category_page_locators
from playwright.sync_api import expect


class CategoryPage(BasePage):

    def check_category_page_displayed(self):
        """Проверка отображения страницы категории товара"""
        good_in_category_page = self.find(category_page_locators.good_in_category_page_loc)
        expect(good_in_category_page, "На странице категории не отображено ни одного товара").not_to_have_count(0)

        expect(self.find(category_page_locators.search_field_loc)).to_be_visible()
        expect(self.find(category_page_locators.search_button_loc)).to_be_visible()
        expect(self.find(category_page_locators.filter_by_material_block_loc)).to_be_visible()
        expect(self.find(category_page_locators.price_range_text_loc)).to_be_visible()

        sort_by_title = self.find(category_page_locators.sort_by_text_loc)
        expect(sort_by_title, f"Текст не соответствует ожидаемому: {sort_by_title.inner_text}").to_have_text("Sort By:")
        expect(self.find(category_page_locators.sort_by_dropdown_field)).to_be_visible()

        expect(self.find(category_page_locators.grid_type_loc)).to_be_visible()
        expect(self.find(category_page_locators.list_type_loc)).to_be_visible()

    def check_sort_by_price(self, direction: Literal["ASC", "DESC"]):
        """Сортировка товаров по цене(ASC/DESC)"""
        # сортировка
        text = category_page_locators.sort_by_price_asc_text \
            if direction.lower() == "asc" else category_page_locators.sort_by_price_desc_text

        self.find(category_page_locators.sort_by_dropdown_field).click()
        option = self.find(f'(//*[contains(text(), "{text}")])[1]')
        option.click()

        # Получение цен товаров после сортировки
        expect(self.find(category_page_locators.good_in_category_page_loc)).not_to_have_count(0)
        product_cards = self.find(category_page_locators.good_in_category_page_loc).all()

        sequence_after = []
        for card in product_cards:
            price_text = card.inner_text()
            dollar_index = price_text.index("$")
            price = int(price_text[dollar_index + 2:-3].replace(',', ''))
            sequence_after.append(price)

        # Ожидаемый порядок
        reverse = text == "Price - High to Low"
        expected_sequence = sorted(sequence_after, reverse=reverse)
        assert sequence_after == expected_sequence, \
            f"Сортировка прошла некорректно. Ожидалось: {expected_sequence}, Получено: {sequence_after}"

    def search_by_keyword(self, search_word: str):
        """Поиск товаров по ключевому слову"""

        search_field = self.find(category_page_locators.search_field_loc)
        search_field.fill(search_word)
        self.find(category_page_locators.search_button_loc).click()

    def check_searching_results(self, search_word: str):
        """Проверка результатов поиска товаров по ключевому слову"""
        # ждём пока подгрузятся изменения
        initial_count = self.find(category_page_locators.good_in_category_page_loc).count()
        expect(self.find(category_page_locators.good_in_category_page_loc)).not_to_have_count(initial_count)

        # проверка вхождения слова без учёта регистра
        product_cards = self.find(category_page_locators.good_in_category_page_loc)
        for product_card in product_cards.all():
            expect(product_card, "Элемент не содержит слово-фильтр").to_contain_text(
                re.compile(search_word, re.IGNORECASE))
