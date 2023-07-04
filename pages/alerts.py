from pages.base_page import BasePage
from components.components import WebElement


class Alerts(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)
        self.alert_btn = WebElement(driver, locator='#alertButton')
        self.alert_btn_conf = WebElement(driver, locator='#confirmButton')
        self.field_conf = WebElement(driver, locator='#confirmResult')
        self.prompt_btn = WebElement(driver, locator='#promtButton')
        self.prompt_res = WebElement(driver, locator='#promptResult')

