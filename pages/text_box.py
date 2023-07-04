from pages.base_page import BasePage
from components.components import WebElement


class TextBox(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)
        self.full_name = WebElement(driver, locator='#userName')
        self.placeholder_btn = WebElement(driver, locator='#userName')
        self.current_address = WebElement(driver, locator='#currentAddress-wrapper>div>#currentAddress')
        self.submit_btn = WebElement(driver, locator='#submit')
        self.output_name = WebElement(driver, locator='#name')
        self.output_address = WebElement(driver, locator='#output > div > #currentAddress')
        self.output_elements = WebElement(driver, locator='#output > div >p')


