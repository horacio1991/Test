# -*- encoding: utf-8 -*
import datetime

from behave import step
from selenium import webdriver


@step(u'I navigate to website')
def navigate(context):
    """
    Navigate to website
    :param context: behave context
    """
    try:
        context.driver = webdriver.Chrome("C:\\Users\\htovoX\\Documents\\Entrevista "
                                  "RH\\venv\\selenium\\webdriver\\chromedriver.exe")
        context.driver.maximize_window()
        context.driver.get("http://automationpractice.com/index.php")
    except Exception as e:
        failure_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        context.driver.get_screenshot_as_file('screenshot-%s.png' % failure_time)
        raise Exception('There was an error when trying to navigate. Error value:' + str(e))