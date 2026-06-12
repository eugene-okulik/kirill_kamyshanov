from test_UI_kkamyshanov_pw.pages.locators import cart_locators, common_locators
from test_UI_kkamyshanov_pw.pages.base_page import BasePage
from playwright.sync_api import expect


class CartPage(BasePage):
    endpoint = "/cart"

    def check_empty_cart_page(self):
        """Проверка отображения пустой корзины"""

        empty_cart = self.find(cart_locators.empty_cart_loc)
        expect(empty_cart).to_have_text("Your cart is empty!")

        order_overview = self.find(cart_locators.order_overview_loc)
        expect(order_overview, "Блок 'order_overview' не отображается").to_be_visible()

    def check_enriched_cart_page(self):
        """Проверка отображения обогащённой корзины"""
        expect(self.find(cart_locators.good_image_loc), "Изображение товара не отображается").to_be_visible()
        expect(self.find(cart_locators.remove_button_in_cart_loc),
               "Кнопка удаления товара из корзины не отображается").to_be_visible()
        expect(self.find(cart_locators.checkout_button_loc), "Кнопка 'checkout' не отображается").to_be_visible()
        expect(self.find(cart_locators.subtotal_area_loc), "Элемент 'Subtotal' не отображается").to_be_visible()
        expect(self.find(cart_locators.taxes_area_loc), "Элемент 'Taxes' не отображается").to_be_visible()
        expect(self.find(cart_locators.total_area_loc), "Элемент 'Total' не отображается").to_be_visible()
        expect(self.find(cart_locators.input_promo_field_loc), "Поле ввода промокода не отображается").to_be_visible()
        expect(self.find(cart_locators.apply_promocode_field_loc),
               "Кнопка подтверждения промокода не отображается").to_be_visible()

    def add_goods_in_cart(self, count: int):
        """Увеличить количество добавленного товара в корзине на count единиц"""
        for _ in range(count):
            self.find(common_locators.add_one_button_loc).click()

    def remove_goods_in_cart(self, count: int = None):
        """Удалить 1/несколько/все единицы товара из корзины. Пока функция удаляет единицы одного экземпляра товара.
        Без аргументов удаляются все единицы товара
        """
        if count:
            for _ in range(count):
                self.find(common_locators.remove_one_button_loc).click()
            return

        actual_count_in_cart = self.find(cart_locators.count_goods_in_cart_button_loc)
        while actual_count_in_cart.is_visible():
            self.find(common_locators.remove_one_button_loc).click()
            self.page.wait_for_timeout(100)  # Ожидание перед след проверкой, чтобы не ждать 30 секунд-таймаута

    def check_goods_count_in_cart(self, count: str):
        """Проверка количества единиц товара в корзине"""
        expect(self.find(cart_locators.count_goods_in_cart_button_loc)).to_have_value(count)
