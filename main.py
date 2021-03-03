from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import os
import time
EMAIL_ADDRESS = "lanrezacthibaud@gmail.com"
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

chrome_driver_path = "/Users/goona/Desktop/Development/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=2413447685&f_LF=f_AL&geoId=105015875&keywords=python%20developer&location=France")

# Get into the job application page
sign_in_button_first_page = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
sign_in_button_first_page.click()

email = driver.find_element_by_id("username")
email.send_keys(EMAIL_ADDRESS)

password = driver.find_element_by_id("password")
password.send_keys(EMAIL_PASSWORD)

sign_in_button_second_page = driver.find_element_by_css_selector(".login__form_action_container .btn__primary--large")
sign_in_button_second_page.click()

# Application process

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in all_listings:
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card .jobs-apply-button")
        apply_button.click()

        phone = driver.find_element_by_class_name("fb-single-line-text__input")

        if phone.text == "":
            phone.send_keys("08037207494")

        footer = driver.find_element_by_tag_name("footer")
        submit_button = footer.find_element_by_css_selector(".display-flex .artdeco-button--primary")
        if submit_button.get_attribute("data-control-name") == "continue-unify":
            print("next-button spotted")
            cancel_button = driver.find_element_by_css_selector(".data-test-modal .artdeco-modal__dismiss")
            cancel_button.click()

            discard_button = driver.find_element_by_css_selector(".artdeco-button--primary")
            discard_button.click()
            print("complex steps - skipped")
            continue
        else:
            submit_button.click()

        escape_button = driver.find_element_by_css_selector(".artdeco-modal__dismiss")
        escape_button.click()
    except NoSuchElementException:
        print("no application button - skipped")
        continue

    time.sleep(3)




# time.sleep(2)
#
# apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card .jobs-apply-button")
# apply_button.click()
#

#
# print("next_button clicked")
#
# time.sleep(2)
#
# phone = driver.find_element_by_class_name("fb-single-line-text__input")
# print(phone.text)
# if phone.text == "":
#     phone.send_keys("08037207494")
#
# print("entry_completed")
#
# review_button = driver.find_element_by_css_selector(".artdeco-button--primary")
# review_button.click()
#
# print("review_button clicked")
#
# submit_button = driver.find_element_by_css_selector(".display-flex .artdeco-button")
# submit_button.click()