from playwright.sync_api import Page, expect, Route
from time import sleep


def test_create_new_phone_model(page: Page):
    test_text = 'яблокофон 17 про'

    def handle_route(route: Route):
        response_body = route.fetch().json()
        response_body['body']['digitalMat'][0]['productName'] = test_text
        response_body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = test_text
        response_body['body']['digitalMat'][0]['familyTypes'][0]['tabTitle'] = test_text
        route.fulfill(json=response_body)

    page.route("**/digital-mat**", handle_route)

    page.goto("https://www.apple.com/shop/buy-iphone")
    page.locator('[class="rf-hcard-img-wrapper"]').nth(0).click()
    title = page.locator('[class="rf-digitalmat-overlay-header typography-manifesto"]').nth(0)
    expect(title, "Текст заголовка не соответствует ожидаемому").to_have_text(test_text)
    sleep(3)  # Слип оставил для удобства проверки задания
