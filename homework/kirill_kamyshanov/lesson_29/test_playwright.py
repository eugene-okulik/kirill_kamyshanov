import re

from playwright.sync_api import Page, Dialog, expect


def test_dialog(page: Page):
    dialog_message = None

    def proceed_dialog(dialog: Dialog):
        nonlocal dialog_message
        dialog_message = dialog.message
        dialog.accept()

    page.on("dialog", proceed_dialog)

    page.goto("https://www.qa-practice.com/elements/alert/confirm")
    page.get_by_role("link", name="Click").click()
    result_section = page.locator("#result")
    expect(result_section, "Блок с результатом не содержит ожидаемый текст").to_contain_text("Ok")


def test_two_tabs(page: Page):
    page.goto("https://www.qa-practice.com/elements/new_tab/button")
    click_button = page.get_by_role("link", name="Click")

    with page.context.expect_page() as tab:
        click_button.click()
    new_page = tab.value

    expect(new_page.locator("#result-text"), "Некорректный текст").to_have_text("I am a new page in a new tab")
    expect(click_button, "Кнопка на первой вкладке не активна").to_be_enabled()


def test_explicit_wait_red(page: Page):
    page.goto("https://demoqa.com/dynamic-properties")
    button = page.get_by_role("button", name="Color Change")
    expect(button).to_have_class(re.compile(r".*text-danger.*"), timeout=10000)
    button.click()
