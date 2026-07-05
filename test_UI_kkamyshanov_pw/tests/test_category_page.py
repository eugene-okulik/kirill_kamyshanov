import pytest


@pytest.mark.regression
@pytest.mark.smoke
def test_category_page_displayed(category_page):
    """Проверка отображения страницы категории товара"""
    category_page.open_page("/category/desks-1")
    category_page.check_category_page_displayed()


@pytest.mark.parametrize("direction", ["ASC", "DESC"])
@pytest.mark.regression
def test_category_page_sort(category_page, direction):
    """Проверка сортировки товаров на странице категории по цене. Как аргумент принимает направление сортировки"""
    category_page.open_page("/category/desks-1")
    category_page.check_sort_by_price(direction)


@pytest.mark.regression
@pytest.mark.smoke
def test_category_page_search_by_valid_keyword(category_page):
    """Проверка функции поиска товаров на странице категории"""
    category_page.open_page("/category/desks-1")
    category_page.search_by_keyword("desk")
    category_page.check_searching_results("desk")
