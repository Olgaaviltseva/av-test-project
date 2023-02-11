from pages.search_form_page import SearchPage
from selenium.webdriver.common.by import By
from time import sleep


def test_search_choose_brand(driver):
    search_page = SearchPage(driver)
    search_page.open()
    search_page.scroll_page_450()
    search_page.click_first_brand_drop_down()
    search_page.click_bentley_brand()
    search_page.wait_show_button_bentley()
    search_page.click_show_button()
    assert search_page.get_text_bentley_brand() == 'Bentley'


def test_search_exclude_brand(driver):
    search_page = SearchPage(driver)
    search_page.open()
    search_page.scroll_page_450()
    search_page.click_first_brand_drop_down()
    search_page.click_exclude_checkbox()
    search_page.click_bentley_brand()
    search_page.wait_show_button_excl_bentley()
    search_page.click_show_button()
    assert search_page.get_text_excl_bentley_brand() == 'Кроме'


def test_search_model(driver):
    search_page = SearchPage(driver)
    search_page.open()
    search_page.scroll_page_450()
    search_page.click_first_brand_drop_down()
    search_page.click_audi_brand()
    search_page.wait_a3_active()
    search_page.click_first_model_drop_down()
    search_page.click_a3_model()
    search_page.wait_show_button_audi_a3()
    search_page.click_show_button()
    assert search_page.get_text_a3_model() == 'A3'


def test_search_generation(driver):
    search_page = SearchPage(driver)
    search_page.open()
    search_page.scroll_page_450()
    search_page.click_first_brand_drop_down()
    search_page.click_audi_brand()
    search_page.wait_a3_active()
    search_page.click_first_model_drop_down()
    search_page.click_a3_model()
    search_page.wait_8l_active()
    search_page.click_first_generation_drop_down()
    search_page.click_gen_8l_button()
    search_page.wait_show_button_8l()
    search_page.click_show_button()
    assert search_page.get_text_list_result() == 'Audi A3 8L'


def test_search_year_from(driver):
    search_page = SearchPage(driver)
    search_page.open()
    search_page.scroll_page_450()
