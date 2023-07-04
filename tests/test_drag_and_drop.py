from pages.droppable import DroppAble
from selenium.webdriver import ActionChains
import time


def test_drag_n_drop(browser):
    d_n_d = DroppAble(browser)
    d_n_d.visit()
    action_chains = ActionChains(browser)

    action_chains.drag_and_drop(
        d_n_d.drag.find_element(),
        d_n_d.drop.find_element()
    ).perform()
    time.sleep(2)
