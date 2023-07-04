from pages.base_page import BasePage
from components.components import WebElement


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)
        self.lorem_field = WebElement(driver, locator='#section1Content > p ')
        self.lorem_btn = WebElement(driver, locator='#section1Heading')
        self.lorem_btn_1 = WebElement(driver, locator='#section2Content > p:nth-child(1)')
        self.lorem_btn_2 = WebElement(driver, locator='#section2Content > p:nth-child(2)')
        self.lorem_btn_self = WebElement(driver, locator='#section3Content > p')
