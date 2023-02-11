from pages.search_form_page import SearchPage
import allure
from time import sleep


@allure.feature('Search form page')
@allure.story('Search by brand')
def test_search_choose_brand(driver):
    with allure.step('Open Search form page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Select brand'):
        search_page.click_first_brand_drop_down()
        search_page.click_bentley_brand()
    with allure.step('Click show button'):
        search_page.wait_show_button_bentley()
        search_page.click_show_button()
    with allure.step('Check that brand is selected'):
        assert search_page.get_text_bentley_brand() == 'Bentley'


@allure.feature('Search form page')
@allure.story('Search with an excluded brand')
def test_search_exclude_brand(driver):
    with allure.step('Open Search form page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Exclude Bentley brand'):
        search_page.click_first_brand_drop_down()
        search_page.click_exclude_checkbox()
        search_page.click_bentley_brand()
    with allure.step('Click show button'):
        search_page.wait_show_button_excl_bentley()
        search_page.click_show_button()
    with allure.step('Check that brand is excluded'):
        assert search_page.get_text_excl_bentley_brand() == 'Кроме'


@allure.feature('Search form page')
@allure.story('Search by brand and model')
def test_search_model(driver):
    with allure.step('Open Search form page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Select Audi brand'):
        search_page.click_first_brand_drop_down()
        search_page.click_audi_brand()
    with allure.step('Select A3 model'):
        search_page.wait_a3_active()
        search_page.click_first_model_drop_down()
        search_page.click_a3_model()
    with allure.step('Click show button'):
        search_page.wait_show_button_audi_a3()
        search_page.click_show_button()
    with allure.step('Check that model is selected'):
        assert search_page.get_text_a3_model() == 'A3'


@allure.feature('Search form page')
@allure.story('Search by brand, model and generation')
def test_search_generation(driver):
    with allure.step('Open Search form page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Select Audi brand'):
        search_page.click_first_brand_drop_down()
        search_page.click_audi_brand()
    with allure.step('Select A3 model'):
        search_page.wait_a3_active()
        search_page.click_first_model_drop_down()
        search_page.click_a3_model()
    with allure.step('Select 8l generation'):
        search_page.wait_8l_active()
        search_page.click_first_generation_drop_down()
        search_page.click_gen_8l_button()
    with allure.step('Click show button'):
        search_page.wait_show_button_8l()
        search_page.click_show_button()
    with allure.step('Check that generation is selected'):
        assert search_page.get_text_list_result() == 'Audi A3 8L'


@allure.feature('Search form page')
@allure.story('Search from the year')
def test_search_year_from(driver):
    with allure.step('Open Search form page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Select from 2022 year'):
        search_page.click_year_from_button()
        search_page.click_year_from_2022_button()
    with allure.step('Click show button'):
        search_page.wait_show_button_from_2022()
        search_page.click_show_button()
    with allure.step('Check that from 2022 year is selected'):
        assert search_page.get_text_2022_year_from() == '2022'


@allure.feature('Search form page')
@allure.story('Search by min year')
def test_search_year_before(driver):
    with allure.step('Open Search form page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Select before 2022 year'):
        search_page.click_year_before_button()
        search_page.click_year_before_2022_button()
    with allure.step('Click show button'):
        search_page.wait_show_button_before_2022()
        search_page.click_show_button()
    with allure.step('Check that before 2022 year is selected'):
        assert search_page.get_text_2022_year_before() == '2022'


@allure.feature('Search form page')
@allure.story('Search by min price')
def test_search_price_from(driver):
    with allure.step('Open Search from page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Select price from'):
        search_page.click_price_from_button()
        search_page.send_price_from_500()
    with allure.step('Click show button'):
        search_page.wait_show_button_from_price_500()
        search_page.click_show_button()
    with allure.step('Check that from price is selected'):
        assert search_page.get_text_price_from_500() == 'Цена от'


@allure.feature('Search form page')
@allure.story('Search by max price')
def test_search_price_before(driver):
    with allure.step('Open Search form page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Select price before'):
        search_page.click_price_before_button()
        search_page.send_price_before_5000()
    with allure.step('Click show button'):
        search_page.wait_show_button_before_price_5000()
        search_page.click_show_button()
    with allure.step('Check that before price is selected'):
        assert search_page.get_text_price_before_5000() == 'до'


@allure.feature('Search form page')
@allure.story('Currency selection')
def test_search_currency_byn(driver):
    with allure.step('Open Search form page'):
        search_page = SearchPage(driver)
        search_page.open()
        search_page.scroll_page_450()
    with allure.step('Select BYN'):
        search_page.click_currency_button()
        search_page.click_byn_button()
    with allure.step('Select price before'):
        search_page.wait_byn_currency()
        search_page.click_price_before_button()
        search_page.send_price_before_5000()
    with allure.step('Click show button'):
        search_page.wait_show_button_5000_byn()
        search_page.click_show_button()
    with allure.step('Check that BYN currency is selected'):
        assert search_page.get_text_byn_currency() == 'BYN'




