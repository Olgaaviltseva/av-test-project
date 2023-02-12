from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import search_options_page as loc
from selenium.webdriver.common.by import By


class OptionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get('https://av.by/')

    def scroll_page_450(self):
        self.driver.execute_script("window.scrollTo(0, 450);")

    def scroll_page_2000(self):
        self.driver.execute_script("window.scrollTo(0, 2000);")

    def click_all_options_button(self):
        self.find(loc.all_options_button).click()

    def click_automatic_transmission_button(self):
        self.find(loc.automation_transmission_button).click()

    def click_show_button(self):
        self.find(loc.show_button).click()

    def wait_show_button_automatic_transmission(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.autom_transm_show_button))

    def get_text_automatic_transmission(self):
        return self.find(loc.automatic_transmission_text).get_attribute('innerText')

    def click_manual_transmission_button(self):
        self.find(loc.manual_transmission_button).click()

    def wait_show_button_manual_transmission(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.manual_transm_show_button))

    def get_text_manual_transmission(self):
        return self.find(loc.manual_transmission_text).get_attribute('innerText')

    def click_body_button(self):
        self.find(loc.body_button).click()

    def click_cabriolet_checkbox(self):
        self.find(loc.cabriolet_checkbox).click()

    def wait_show_button_cabriolet(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.cabriolet_show_button))

    def get_text_cabriolet(self):
        return self.find(loc.cabriolet_text).get_attribute('innerText')

    def click_engine_type_button(self):
        self.find(loc.engine_type_button).click()

    def click_diesel_button(self):
        self.find(loc.diesel_button).click()

    def wait_show_button_diesel(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.diesel_show_button))

    def get_text_diesel(self):
        return self.find(loc.diesel_text).get_attribute('innerText')

    def click_drive_unit_button(self):
        self.find(loc.drive_unit_button).click()

    def click_front_wheel_drive_button(self):
        self.find(loc.front_wheel_drive_button).click()

    def wait_show_button_front_wheel_drive(self):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(loc.front_wheel_drive_show_button))

    def get_text_front_wheel_button(self):
        return self.find(loc.front_wheel_drive_text).get_attribute('innerText')
