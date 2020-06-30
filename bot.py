import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep


# //Global variables
email = "your_email_here"
password = "your_password_here"
keywords = ["enter","the","keywords"]



def get_browser():
    """Load the browser"""
    global browser
    chromedriver_autoinstaller.install()
    # Register the driver
    browser = webdriver.Chrome()
    # browser.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Ffeed%2F&fromSignIn=true&trk=cold_join_sign_in")
    browser.get(r"https://linkedin.com")




def sign_in(username, password):
    """Signs into account"""
    signIn = browser.find_element_by_link_text('Sign in')
    signIn.click()
    sleep(2)
    """If you wanna sign in directly from the linkedin.com use this you can use this line"""
    enter_mail = browser.find_element_by_id('username')
    enter_pass = browser.find_element_by_id('password')
    enter_mail.send_keys(email)
    enter_pass.send_keys(password)
    click_login = browser.find_element_by_class_name('btn__primary--large')
    click_login.click()


def click_somewhere():
    """Basically if you wanna click jobs just change the ember23 with your custom path"""
    click_network = browser.find_element_by_id("ember23")
    click_network.click()


def scroll_page_down(times: int = 20, y_height: int = 50000):
    """When y get biggers it scrolls down more"""
    for i in range(1, times+1):
        browser.execute_script(f"window.scrollTo(0, {y_height});")
        print(f"{i}. iteration")
        sleep(3)

def send_invite():
    """Sends invite"""
    send_inv = browser.find_element_by_css_selector("span.discover-person-card__name.t-16.t-black.t-bold")
    send_inv.click()





def main():
    get_browser()
    sign_in(email, password)
    sleep(5)
    try:
        click_somewhere()
    except NoSuchElementException:
        sleep(1)
    sleep(3)
    scroll_page_down()
    sleep(5)

    "Variables to log in"
    info = browser.find_elements_by_class_name("discover-entity-type-card__info-container")
    bottom = browser.find_elements_by_class_name("discover-entity-type-card__bottom-container")
    cnt = 1


    for person_info, person_bottom in zip(info,bottom):
        job = person_info.find_element_by_css_selector("span.discover-person-card__occupation.t-14.t-black--light.t-normal").text.lower().split()
        send_inv = person_bottom.find_element_by_css_selector("button.full-width.artdeco-button.artdeco-button--2.artdeco-button--full.artdeco-button--secondary.ember-view")
        if not [i for i in job if i in keywords] == []:
            try:
                send_inv.click()
                sleep(0.8)
                print(f"Invite sent successfully to {cnt} people")
                cnt += 1
            except ElementClickInterceptedException:
                sleep(0.1)


    # browser.close()
if __name__ == '__main__':
    main()

