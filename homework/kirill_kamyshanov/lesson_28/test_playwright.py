from playwright.sync_api import Page, expect


def test_get_by_role(page: Page):
    page.goto("https://the-internet.herokuapp.com/")
    page.get_by_role("link", name="Form Authentication").click()
    # Заполнение формы
    page.get_by_role("textbox", name="Username").fill("tomsmith")
    page.get_by_role("textbox", name="Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=" Login").click()
    # Проверка
    expect(page.get_by_role("heading", level=4)).to_be_visible()


def test_freestyle_fill_form(page: Page):
    page.goto("https://demoqa.com/automation-practice-form")

    page.get_by_placeholder("First Name").fill("Егор")
    page.get_by_placeholder("Last Name").fill("Игнатьев")
    page.get_by_placeholder("name@example.com").fill("yalublysoup@ya.ru")
    page.locator("#gender-radio-1").check()
    page.get_by_role("textbox", name="Mobile").fill("9998887766")

    # Дата рождения
    page.locator("#dateOfBirthInput").click()
    page.select_option("[class='react-datepicker__month-select']", value="10")
    page.select_option("[class='react-datepicker__year-select']", value="1996")
    page.locator("//div[text()='3' and contains(@aria-label, 'November')]").click()

    # Предметы
    subjects = page.locator("(//input[@role='combobox'])[1]")
    subjects.fill("Maths")
    subjects.press("Enter")

    # Увлечения
    page.get_by_label("Reading").check()
    # Адрес
    page.get_by_placeholder("Current Address").fill("Деревня Простоквашино")

    # Страна
    state = page.locator("(//*[@autocapitalize='none'])[2]")
    state.fill("NCR")
    state.press("Enter")

    # Город
    city = page.locator("#react-select-4-input")
    city.fill("Delhy")

    # Подтверждение
    page.get_by_role("button", name="Submit").click()

    # Проверка
    expect(page.get_by_text("Thanks for submitting the form")).to_be_visible()
