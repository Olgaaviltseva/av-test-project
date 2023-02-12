from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import search_form_page as loc
from selenium.webdriver.common.by import By


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://av.by/')

    def scroll_page_450(self):
        self.driver.execute_script("window.scrollTo(0, 450);")

    def click_first_brand_drop_down(self):
        self.find(loc.first_brand_drop_down).click()

    def click_first_model_drop_down(self):
        self.find(loc.first_model_drop_down).click()

    def click_first_generation_drop_down(self):
        self.find(loc.first_generation_drop_down).click()

    def click_bentley_brand(self):
        self.find(loc.bentley_button).click()

    def click_audi_brand(self):
        self.find(loc.audi_button).click()

    def click_a3_model(self):
        self.find(loc.a3_button).click()

    def click_gen_8l_button(self):
        self.find(loc.gen_8l_button).click()

    def click_exclude_checkbox(self):
        self.find(loc.exclude_checkbox).click()

    def click_show_button(self):
        self.find(loc.show_button).click()

    def click_year_from_button(self):
        self.find(loc.year_from_button).click()

    def click_year_before_button(self):
        self.find(loc.year_before_button).click()

    def click_year_from_2022_button(self):
        self.find(loc.year_from_2022_button).click()

    def click_year_before_2022_button(self):
        self.find(loc.year_before_2022_button).click()

    def click_price_from_button(self):
        self.find(loc.price_from_button).click()

    def click_price_before_button(self):
        self.find(loc.price_before_button).click()

    def click_currency_button(self):
        self.find(loc.currency_button).click()

    def click_byn_button(self):
        self.find(loc.byn_button).click()

    def click_volume_from_button(self):
        self.find(loc.volume_from_button).click()

    def click_volume_before_button(self):
        self.find(loc.volume_before_button).click()

    def click_l_1_2_button(self):
        self.find(loc.l_1_2_vol_from_button).click()

    def click_l_1_3_button(self):
        self.find(loc.l_1_3_vol_before_button).click()

    def get_text_bentley_brand(self):
        return self.find(loc.bentley_brand).get_attribute('innerText')

    def get_text_excl_bentley_brand(self):
        return self.find(loc.bentley_brand_excl).get_attribute('innerText')

    def get_text_a3_model(self):
        return self.find(loc.a3_model).get_attribute('innerText')

    def get_text_2022_year_from(self):
        return self.find(loc.year_2022_from).get_attribute('innerText')

    def get_text_2022_year_before(self):
        return self.find(loc.year_2022_before).get_attribute('innerText')

    def get_text_price_from_500(self):
        return self.find(loc.price_from_500).get_attribute('innerText')

    def get_text_price_before_5000(self):
        return self.find(loc.price_before_5000).get_attribute('innerText')

    def get_text_byn_currency(self):
        return self.find(loc.byn_currency).get_attribute('innerText')

    def get_text_l_1_2_volume_from(self):
        return self.find(loc.l_1_2_volume_from).get_attribute('innerText')

    def get_text_l_1_3_volume_before(self):
        return self.find(loc.l_1_3_volume_before).get_attribute('innerText')

    def wait_listing_title(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.listing__title))

    def wait_show_button_bentley(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_bentley))

    def wait_show_button_audi_a3(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_audi_a3))

    def wait_show_button_excl_bentley(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_excl_bentley))

    def wait_show_button_8l(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_audi_a3_8l))

    def wait_show_button_from_2022(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_from_2022))

    def wait_show_button_before_2022(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_before_2022))

    def wait_a3_active(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.a3_list))

    def wait_8l_active(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.list_8l))

    def wait_byn_currency(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_byn))

    def wait_show_button_from_price_500(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_from_price_500))

    def wait_show_button_before_price_5000(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_before_price_5000))

    def wait_show_button_5000_byn(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_5000_byn))

    def wait_show_button_l_1_2_volume_from(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_l_1_2_volume_from))

    def wait_show_button_l_1_3_volume_before(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.show_button_l_1_3_volume_before))

    def get_text_list_result(self):
        list_result = self.driver.find_element(By.CLASS_NAME, 'listing__items')
        list_cars = list_result.find_elements(By.CLASS_NAME, 'link-text')
        return list_cars[5].get_attribute('innerText')

    def send_price_from_500(self):
        self.send(loc.price_from_button, '500')

    def send_price_before_5000(self):
        self.send(loc.price_before_button, '5000')
