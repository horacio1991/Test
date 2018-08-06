from behave import step
from selenium.webdriver.common.by import By


@step(u'I able to register my profile successfully')
def click_on_register(context):
    """
    This method submit form to create a new user
    :param context: behave context
    """
    context.driver.find_element(By.NAME, "submitAccount").click()


@step(u'I able to login with the followings credentials "{email}" and "{password}"')
def login(context, email, password):
    """
    This method enter credentials to be able to login
    :param context:
    :param email: email
    :param password: password
    :return: behave context
    """
    context.driver.find_element(By.NAME, "email").send_keys(email)
    context.driver.find_element(By.NAME, "passwd").send_keys(password)
    context.driver.find_element(By.NAME, "SubmitLogin").click()


@step(u'I buy my item')
def buy(context):
    """
    This method follow the purchases process to confirm it
    :param context: behave context
    :return:
    """
    context.driver.find_element(By.CLASS_NAME, "shopping_cart").find_element(By.TAG_NAME, "a").click()
    context.driver.find_element(By.CSS_SELECTOR, ".button.btn.btn-default.standard-checkout.button-medium").click()
    context.driver.find_element(By.NAME, "processAddress").click()
    context.driver.find_element(By.CLASS_NAME, "checker").click()
    context.driver.find_element(By.NAME, "processCarrier").click()
    context.driver.find_element(By.CLASS_NAME, "payment_module").click()
    context.driver.find_element(By.CSS_SELECTOR, ".cart_navigation.clearfix").find_element(By.TAG_NAME, "span").click()
