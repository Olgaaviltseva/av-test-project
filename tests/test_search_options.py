from pages.search_options_page import OptionsPage
import allure
from time import sleep


@allure.feature('Search form page')
@allure.story('Search by automatic transmission')
def test_select_automatic_transmission(driver):
    with allure.step('Open Search form page'):
        options_page = OptionsPage(driver)
        options_page.open()
        options_page.scroll_page_450()
    with allure.step('Select automatic transmission'):
        options_page.click_all_options_button()
        options_page.click_automatic_transmission_button()
    with allure.step('Click show button'):
        options_page.wait_show_button_automatic_transmission()
        options_page.scroll_page_2000()
        options_page.click_show_button()
    with allure.step('Check that automatic transmission is selected'):
        assert options_page.get_text_automatic_transmission() == 'автомат'


@allure.feature('Search form page')
@allure.story('Search by manual transmission')
def test_select_manual_transmission(driver):
    with allure.step('Open Search form page'):
        options_page = OptionsPage(driver)
        options_page.open()
        options_page.scroll_page_450()
    with allure.step('Select manual transmission'):
        options_page.click_all_options_button()
        options_page.click_manual_transmission_button()
    with allure.step('Click show button'):
        options_page.wait_show_button_manual_transmission()
        options_page.scroll_page_2000()
        options_page.click_show_button()
    with allure.step('Check that manual transmission is selected'):
        assert options_page.get_text_manual_transmission() == 'механика'


@allure.feature('Search form page')
@allure.story('Search by manual transmission')
def test_search_body(driver):
    with allure.step('Open Search form page'):
        options_page = OptionsPage(driver)
        options_page.open()
        options_page.scroll_page_450()
    with allure.step('Select cabriolet body'):
        options_page.click_all_options_button()
        options_page.click_body_button()
        options_page.click_cabriolet_checkbox()
    with allure.step('Click show button'):
        options_page.wait_show_button_cabriolet()
        options_page.scroll_page_2000()
        options_page.click_show_button()
    with allure.step('Check that cabriolet is selected'):
        assert options_page.get_text_cabriolet() == 'кабриолет'


@allure.feature('Search form page')
@allure.story('Search by engine type')
def test_search_body(driver):
    with allure.step('Open Search form page'):
        options_page = OptionsPage(driver)
        options_page.open()
        options_page.scroll_page_450()
    with allure.step('Select diesel engine'):
        options_page.click_all_options_button()
        options_page.click_engine_type_button()
        options_page.click_diesel_button()
    with allure.step('Click show button'):
        options_page.wait_show_button_diesel()
        options_page.scroll_page_2000()
        options_page.click_show_button()
    with allure.step('Check that cabriolet is selected'):
        assert options_page.get_text_diesel() == 'дизель'


@allure.feature('Search form page')
@allure.story('Search by front-wheel drive')
def test_search_body(driver):
    with allure.step('Open Search form page'):
        options_page = OptionsPage(driver)
        options_page.open()
        options_page.scroll_page_450()
    with allure.step('Select front-wheel_drive'):
        options_page.click_all_options_button()
        options_page.click_drive_unit_button()
        options_page.click_front_wheel_drive_button()
    with allure.step('Click show button'):
        options_page.wait_show_button_front_wheel_drive()
        options_page.scroll_page_2000()
        options_page.click_show_button()
    with allure.step('Check that front-wheel drive is selected'):
        assert options_page.get_text_front_wheel_button() == 'передний привод'
