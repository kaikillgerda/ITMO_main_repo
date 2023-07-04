from pages.browser_tab import BrowserTab
import time


def test_browser_tab(browser):
    tab_page = BrowserTab(browser)
    tab_page.visit()
    assert len(browser.window_handles) == 1
    tab_page.new_tab.click()
    time.sleep(2)
    assert len(tab_page.driver.window_handles) == 2  # можно обратиться  и так
    browser.switch_to.window(browser.window_handles[0])
    time.sleep(2)


