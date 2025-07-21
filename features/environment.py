from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from app.application import Application
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def browser_init(context):
    """
    :param context: Behave context
    """


   # driver_path = ChromeDriverManager().install()
   # service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)

    ### HEADLESS MODE ####
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
     #    options=options,
      #   service=service
     #)
########################################################################
    driver_path = GeckoDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Firefox(service=service)

    options = Options()
    options.headless = False  # comment out to see the GUI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    #context.driver = webdriver.Firefox(options=options)





    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 30)
    context.app = Application(context.driver)

###############################################################################

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
