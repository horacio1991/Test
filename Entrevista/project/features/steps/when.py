import time
from behave import step
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from features.steps.common import field_verification


@step(u'I click on sign-in')
def sign_on(context):
    """
    This method click on sign-in
    :param context: behave context
    :return:
    """
    try:
        context.driver.find_element(By.CLASS_NAME, "login").click()
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "email")))
    except Exception as e:
        context.driver.get_screenshot_as_file('sign-in.png')
        raise Exception('There was an error when trying to navigate. Error value:' + str(e))


@step(u'I click on Register using "{email}"')
def register_option(context, email):
    """
    This method click on register using the email provided by parameter
    :param context: behave context
    :param email: email
    :return:
    """
    email_box = context.driver.find_element(By.NAME, "email_create")
    email_box.clear()
    email_box.send_keys(email)
    email_box.click()
    assert not field_verification(context), " Email verification failed"
    context.driver.find_element(By.CSS_SELECTOR, ".icon-user.left").click()


@step(u'I filed my personal information "{name}" "{last_name}" "{password}" "{email}" for "{gender}"')
def enter_personal_information(context, name, last_name, email, password, gender):
    """
    This method fill personal information
    :param context: behave context
    :param name: information sent by parameter
    :param last_name: information sent by parameter
    :param email: information sent by parameter
    :param password: information sent by parameter
    :param gender: information sent by parameter
    :return:
    """
    assert gender in ["Mr", "Mrs"], "Value entered for Sex is not allowed"
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.element_to_be_clickable((By.ID, "id_gender1")))
    if gender == "Mr":
        context.driver.find_element(By.ID, "id_gender1").click()
    elif gender == "Mrs":
        context.driver.find_element(By.ID, "id_gender2").click()
    context.driver.find_element(By.NAME, "customer_firstname").send_keys(name)
    context.driver.find_element(By.NAME, "customer_lastname").send_keys(last_name)
    context.driver.find_element(By.NAME, "passwd").send_keys(password)
    assert not field_verification(context), "Personal Information verification failed"


@step(u'I filed my address information "{company}" "{address}" "{city}" "{state}" "{cp}" "{country}" "{home_phone}" '
      u'"{mobile_phone}" "{future_address}" "{address_2}" "{comment}"')
def enter_address_information(context, company, address, city, state, cp, country, home_phone, mobile_phone,
                              future_address, address_2, comment):
    """
    This method fill the information needed to create a user
    :param context:  beahve context
    :return:
    """
    if company and home_phone and address_2 and comment == "NO":
        enter_required_data(context, address, city, state, cp, country, mobile_phone, future_address)
    else:
        enter_required_data(context, address, city, state, cp, country, mobile_phone, future_address)
        enter_additional_data(context, company, home_phone, address_2, comment)


def enter_required_data(context, address, city, state, cp, country, mobile_phone, future_address):
    """
    This method enter the information required to create an user
    :param context:  behave context
    :param address: information sent by parameter
    :param city: information sent by parameter
    :param state: information sent by parameter
    :param cp: information sent by parameter
    :param country: information sent by parameter
    :param mobile_phone: information sent by parameter
    :param future_address: information sent by parameter
    :return:
    """
    context.driver.find_element(By.NAME, "address1").send_keys(address)
    context.driver.find_element(By.NAME, "city").send_keys(city)
    context.driver.find_element(By.NAME, "id_state").send_keys(state)
    context.driver.find_element(By.NAME, "postcode").send_keys(cp)
    context.driver.find_element(By.NAME, "id_country").send_keys(country)
    context.driver.find_element(By.NAME, "phone_mobile").send_keys(mobile_phone)
    context.driver.find_element(By.NAME, "alias").send_keys(future_address)
    assert not field_verification(context), "Required Data verification failed"


def enter_additional_data(context, company, home_phone, address_2, comment):
    """
    This method enter information does not requested to create an user
    :param context: behave context
    :param company: information sent by parameter
    :param home_phone: information sent by parameter
    :param address_2: information sent by parameter
    :param comment: information sent by parameter
    :return:
    """
    context.driver.find_element(By.NAME, "company").send_keys(company)
    context.driver.find_element(By.NAME, "phone").send_keys(home_phone)
    context.driver.find_element(By.NAME, "address2").send_keys(address_2)
    context.driver.find_element(By.NAME, "other").send_keys(comment)
    assert not field_verification(context), "Additional Data verification failed"


@step(u'I search for "{topic}" and select the first item')
def buy(context, topic):
    """
    This method select the first element to add to the shopping cart
    :param context: behave context
    :param topic: clothes to search
    :return:
    """
    context.driver.find_element(By.NAME, "search_query").send_keys(topic)
    context.driver.find_element(By.NAME, "submit_search").click()
    table = context.driver.find_elements(By.CLASS_NAME, "product-container")
    for element in table:
        element.click()
        time.sleep(1)
        element.find_elements(By.TAG_NAME, "a")[4].click()
        wait = WebDriverWait(context.driver, 10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cross")))
        context.driver.find_element(By.CLASS_NAME, "cross").click()
        break
