from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)
        self.text_center_elements = WebElement(driver, locator='#app > div > div > div.row > div.col-12.mt-4.col-md-6')
        self.text_header_elements = WebElement(driver,
                                               locator='#app > div > div > div.pattern-backgound.playgound-header > div')
        self.btn_first_e = WebElement(driver, locator='div:nth-child(1) > div > div > div:nth-child(1) > span > div')
        self.text_box_btn_e = WebElement(driver, locator='div:nth-child(1) > div #item-0')
        self.check_box_btn_e = WebElement(driver, locator='div:nth-child(1) > div #item-1')
        self.btns_first_menu = WebElement(driver, locator='div:nth-child(1) > div > ul > li')

    # убрали этот метод в base_page
    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     return False
