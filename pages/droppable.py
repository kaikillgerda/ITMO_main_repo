from pages.base_page import BasePage
from components.components import WebElement


class DroppAble(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable'
        super().__init__(driver, self.base_url)
        self.drag = WebElement(driver, locator='#draggable')
        self.drop = WebElement(driver, locator='#droppable')
