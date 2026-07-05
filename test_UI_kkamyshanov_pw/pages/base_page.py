class BasePage:
    host = "http://testshop.qa-practice.com/shop"
    endpoint = None

    def __init__(self, page):
        self.page = page

    def open_page(self, endpoint: str = None):
        """Открыть страницу"""
        endpoint = self.endpoint if not endpoint else endpoint
        endpoint = endpoint if endpoint.startswith('/') else f'/{endpoint}'
        return self.page.goto(f"{self.host}{endpoint}")

    def find(self, locator: str):
        """Найти один элемент по локатору"""
        return self.page.locator(locator)
