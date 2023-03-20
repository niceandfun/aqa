from locators.text_box_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def test_elements(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys('1')
        self.element_is_visible(self.locators.EMAIL).send_keys('2@mail.ru')
        self.element_is_visible(self.locators.CURRENT_ADRESS).send_keys('3')
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys('4')
        self.element_is_visible(self.locators.SUBMIT).click()

    def checked_filled_form(self):
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text
        email = self.element_is_present(self.locators.CREATED_EMAIL).text
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADRESS).text
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text
        return full_name, email, current_address, permanent_address
