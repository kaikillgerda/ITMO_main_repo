from pages.alerts import Alerts
import time


def test_allert(browser):
    alerts_page = Alerts(browser)
    alerts_page.visit()
    assert not alerts_page.alert()
    alerts_page.alert_btn.click()
    time.sleep(2)
    assert alerts_page.alert()
    alerts_page.alert().accept()


def test_alert_text(browser):
    alert_pg = Alerts(browser)
    alert_pg.visit()
    time.sleep(2)
    alert_pg.alert_btn.click()
    time.sleep(2)
    assert alert_pg.alert().text == "You clicked a button"
    alert_pg.alert().accept()
    assert not alert_pg.alert()


def test_confirm(browser):
    alert_conf = Alerts(browser)
    alert_conf.visit()
    alert_conf.alert_btn_conf.click()
    time.sleep(2)
    alert_conf.alert().dismiss()
    time.sleep(2)
    assert alert_conf.field_conf.get_text() == "You selected Cancel"


def test_prompt(browser):
    prompt_pg = Alerts(browser)
    prompt_pg.visit()
    prompt_pg.prompt_btn.click()
    time.sleep(2)
    prompt_pg.alert().send_keys("Kirill")
    prompt_pg.alert().accept()
    assert prompt_pg.prompt_res.get_text() == "You entered Kirill"
    time.sleep(2)
