from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)
        self.btns_all = WebElement(driver, locator=' div:nth-child(3) > div > ul > li')
        self.icon_btn = WebElement(driver, locator='#app > header > a')
