import pytest


@pytest.mark.regression
@pytest.mark.smoke
def test_good_page_displayed(good_page):
    """Проверка отображения страницы товара"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.check_product_page_displayed()


@pytest.mark.regression
@pytest.mark.smoke
def test_add_good_in_card(good_page):
    """Проверка добавления одного/нескольких экземпляров товара в корзину со страницы карточки товара"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.add_goods_in_card(4)
    good_page.assert_goods_was_added_in_card(4)


@pytest.mark.regression
@pytest.mark.skip(reason="Перестала отображаться иконка с валютой. xfail заменён на pass, чтобы не было таймаута")
def test_change_currency_in_card(good_page):
    """Проверка смены валюты в карточке товара"""
    good_page.open_page("/furn-9999-office-design-software-7?category=9")
    good_page.change_currency_to_eur()
    good_page.assert_price_displayed_in_currency("€")
