import pytest


@pytest.mark.regression
@pytest.mark.smoke
def test_cart_displays_correct_elements_after_adding_good(cart_page):
    """Проверка отображения элементов в пустой корзине"""
    cart_page.open_page()
    cart_page.check_empty_cart_page()


@pytest.mark.regression
@pytest.mark.smoke
def test_cart_with_a_good(good_page, cart_page, add_test_good_in_cart):
    """Проверка отображения элементов в обогащённой корзине после добавления товара"""
    cart_page.open_page()
    cart_page.check_enriched_cart_page()


@pytest.mark.regression
@pytest.mark.smoke
def test_change_goods_count_in_cart(good_page, cart_page, add_test_good_in_cart):
    """Проверка изменения количества товара в корзине (увеличение/уменьшение/полная очистка)"""
    cart_page.open_page()
    cart_page.add_goods_in_cart(3)
    cart_page.check_goods_count_in_cart("4")
    cart_page.remove_goods_in_cart(2)
    cart_page.check_goods_count_in_cart("2")
    cart_page.remove_goods_in_cart()
    cart_page.check_empty_cart_page()
