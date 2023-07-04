from pages.base_page import BasePage
from components.components import WebElement


class FormPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)
        self.first_name = WebElement(driver, locator='#firstName')
        self.last_name = WebElement(driver, locator='#lastName')
        self.user_email = WebElement(driver, locator='#userEmail')
        self.gender_radio_1 = WebElement(driver, locator='#gender-radio-1')
        self.user_number = WebElement(driver, locator='#userNumber')
        self.btn_submit = WebElement(driver, locator='#submit')
        self.modal_dialog = WebElement(driver, locator='body > div.fade.modal.show > div')
        self.btn_close_modal = WebElement(driver, locator='#closeLargeModal')
        self.hobbies_check = WebElement(driver, locator='#hobbies-checkbox-2')
        self.btn_current_address = WebElement(driver, locator='#currentAddress')
        self.btn_state = WebElement(driver, locator='#state')
        self.inp_state = WebElement(driver, locator='#react-select-3-input')
        self.btn_city = WebElement(driver, locator='#stateCity-wrapper > div:nth-child(3)')
        self.inp_city = WebElement(driver,"//*[contains(text(),'Delhi')]", 'xpath')