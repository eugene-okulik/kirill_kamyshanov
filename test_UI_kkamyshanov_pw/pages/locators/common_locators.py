
# иконка корзины с количеством товаров (не 0)
count_goods_in_card = \
    '//nav[@aria-label="Main"]//sup[@class="my_cart_quantity badge text-bg-primary position-absolute top-0 end-0 mt-n1 me-n1 rounded-pill"]'

# Блок смены валюты (есть на разных страницах)
change_currency_button = '//div[@class="o_pricelist_dropdown dropdown d-lg-inline ms-2"]//a[@data-bs-toggle="dropdown"]'
change_to_eur_button = '//a[@href="/shop/change_pricelist/3"]'

# Изменение кол-ва товаров на 1 (страница товара и корзина)
add_one_button_loc = '[title="Add one"]'
remove_one_button_loc = '[title="Remove one"]'
