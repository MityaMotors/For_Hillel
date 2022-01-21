from .base_page import BasePage
from .home_page import HomePage


class AutorizationPage(BasePage):
    def __init__(self, driver=None) -> None:
        super().__init__(driver)

        self.__input_login_locator = "//div[1]/app-login//div[1]/div/input"
        self.__input_password_locator = "//div[1]/app-login//div[2]/div/input"
        self.__enter_button = "//app-access/div/div[1]/app-login/div/div/form/app-button/button"

    def _click_log_into_login_input(self):
        self._click_on_element(self.__input_login_locator)

    def _put_log_into_login_input(self):
        self._enter_text_log_field(self.__input_login_locator)

    def _click_pass_into_pass_input(self):
        self._click_on_element(self.__input_password_locator)

    def _put_pass_into_pass_input(self):
        self._enter_text_pass_field(self.__input_password_locator)

    def make_autorization(self) -> HomePage:
        self._click_pass_into_pass_input()
        self._put_log_into_login_input()
        self._click_pass_into_pass_input()
        self._put_pass_into_pass_input()
        self._click_on_element(self.__enter_button)

        return HomePage(self._driver)
