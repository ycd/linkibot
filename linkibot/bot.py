import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    NoSuchElementException,
)
from time import sleep

__all__ = ["Linkibot"]


class Linkibot(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.browser = self._get_browser()
        self._keywords = []

    def _get_browser(self):
        chromedriver_autoinstaller.install()
        browser = webdriver.Chrome()
        return browser

    def sign_in(self):
        """Signs into account"""
        signIn = self.browser.find_element_by_link_text("Sign in")
        signIn.click()
        sleep(2)

        """If you wanna sign in directly from the linkedin.com use this you can use this line"""
        enter_mail = self.browser.find_element_by_id("username")
        enter_pass = self.browser.find_element_by_id("password")
        enter_mail.send_keys(self.email)
        enter_pass.send_keys(self.password)
        click_login = self.browser.find_element_by_class_name("btn__primary--large")
        click_login.click()

    def click_mynetwork(self):
        """Basically if you wanna click jobs just change the ember23 with your custom path"""
        click_network = self.browser.find_element_by_id("ember23")
        try:
            click_network.click()
        except Exception:
            sleep(1)
            click_network.click()

    def scroll_page_down(self, times: int = 20, y_height: int = 50000):
        """When y get biggers it scrolls down more"""
        for i in range(1, times + 1):
            self.browser.execute_script(f"window.scrollTo(0, {y_height});")
            sleep(0.5)

    def send_invite(self):
        """Sends invite"""
        send_inv = self.browser.find_element_by_css_selector(
            "span.discover-person-card__name.t-16.t-black.t-bold"
        )
        send_inv.click()

    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        assert isinstance(keywords, list), "Keywords must be a list."
        self._keywords = keywords

    def run(self):
        self.browser.get("https://linkedin.com")
        self.sign_in()
        sleep(4)
        try:
            self.click_mynetwork()
        except NoSuchElementException:
            sleep(1)
            self.click_mynetwork()
        sleep(3)
        self.scroll_page_down()
        sleep(2)

        info = self.browser.find_elements_by_class_name(
            "discover-entity-type-card__info-container"
        )
        bottom = self.browser.find_elements_by_class_name(
            "discover-entity-type-card__bottom-container"
        )
        cnt = 1

        for person_info, person_bottom in zip(info, bottom):
            job = (
                person_info.find_element_by_css_selector(
                    "span.discover-person-card__occupation.t-14.t-black--light.t-normal"
                )
                .text.lower()
                .split()
            )
            send_inv = person_bottom.find_element_by_css_selector(
                "button.full-width.artdeco-button.artdeco-button--2.artdeco-button--full.artdeco-button--secondary.ember-view"
            )
            person_description = [
                i.replace(".", "")
                for i in job
                if i.replace(".", "") in self.keywords and i.replace(".", "").isalpha()
            ]
            if person_description != []:
                try:
                    send_inv.click()
                    sleep(1)  # This is for avoiding potential bans from Linkedin.
                    print(f"Invite successfully sent to {cnt} people")
                    cnt += 1
                except Exception:
                    sleep(0.1)
