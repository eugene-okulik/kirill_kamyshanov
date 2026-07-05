import pytest

from test_UI_kkamyshanov_pw.pages.cart_page import CartPage
from test_UI_kkamyshanov_pw.pages.category_page import CategoryPage
from test_UI_kkamyshanov_pw.pages.good_page import GoodPage


@pytest.fixture
def add_test_good_in_cart(good_page):
    """Фикстура для добавления тестового товара в корзину"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.add_goods_in_card(1)
    return


@pytest.fixture
def good_page(page):
    return GoodPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def category_page(page):
    return CategoryPage(page)
