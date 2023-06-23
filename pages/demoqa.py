from pages.base_page import BasePage
from components.components import WebElement


class DemoQA(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)
        self.icon = WebElement(driver, locator='#app > header > a')
        self.btn_elements = WebElement(driver, locator='#app > div > div > div.home-body > div > div:nth-child(1)')
        self.text_footer = WebElement(driver, locator='#app > footer > span')
        self.text_center_elements = WebElement(driver, locator='#app > div > div > div.row > div.col-12.mt-4.col-md-6')

    # def exist_icon(self):
    #     try:
    #         self.icon.find_element()
    #     except NoSuchElementException:
    #         return False
    #     return True

    # def click_on_the_icon(self):
    #     self.find_element(locator='#app > header > a').click()

    # убрали этот метод в base_page
    # def equal_url(self):
    #     if self.get_url() == self.base_url:
    #         return True
    #     return False

    # def click_on_the_bth_elements(self):
    #     self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()
