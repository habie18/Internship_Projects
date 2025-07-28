from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

from app.application import Application
from support.logger import logger


#Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """


    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    # Enable capturing of the browser logs:
    # chrome_options = Options()
    # chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    #
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)


    ### HEADLESS MODE ####
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #service = Service(ChromeDriverManager().install())
    #context.driver = webdriver.Chrome(
    #   options=options,
    #    service=service
    #)
    #context.driver.set_window_size(1920, 1080)
########################################################################

    #options = FirefoxOptions()
    #options.headless = False  # comment out to see the GUI
    #options.add_argument("--no-sandbox")
    #options.add_argument("--disable-dev-shm-usage")

    #context.driver = webdriver.Firefox(options=options)

    ### BROWSERSTACK ###
     #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings

    #bs_user = 'habeebkassim_XKky1W'
    #bs_key = 'wJnEA55jyn9dqK2ccu44'
    #url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    #options = Options()
    #bstack_options = {
    #     "os" : "Windows",
     #    "osVersion" : "11",
     #    'browserName': 'firefox',
     #    'sessionName': scenario_name,
     #}
    #options.set_capability('bstack:options', bstack_options)
    #context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 30)
    context.app = Application(context.driver)

###############################################################################

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    # Add browser logs:
    # browser_logs = context.driver.get_log('browser')
    # with open("browser_logs.txt", "w") as log_file:
    #     for log_entry in browser_logs:
    #         log_file.write(f"{log_entry['level']} - {log_entry['timestamp']} - {log_entry['message']}\n")
    # print("Browser logs have been saved to browser_logs.txt")


    context.driver.quit()
