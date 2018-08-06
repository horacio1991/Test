# -*- encoding: utf-8 -*
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def field_verification(context):
    """
    This method verifies that the value entered on the filed is correct
    """
    try:
        error_name = context.driver.find_element(By.CSS_SELECTOR, ".form-group.form-error").text
        context.error_name = str(error_name)
        return True
    except NoSuchElementException as e:
        return False
