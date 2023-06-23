# from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.demoqa import DemoQA

def test_icon_exist(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    demo_page.icon.click()
    assert demo_page.equal_url()
    assert demo_page.icon.exist()


#     # driver = webdriver.Chrome()
#     browser.get("https://demoqa.com/")
#     icon = browser.find_element(By.CSS_SELECTOR, "#app > header > a")
#
#     if icon is None:
#         print('Элемент не найден')
#     else:
#         print('Элемент найден')



