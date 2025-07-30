from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Remote


from app.application import Application
from support.logger import logger


#Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

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

    ###Mobile emulation Chrome
    mobile_emulation = {"deviceName": "Pixel 7"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # run locally
    context.driver = webdriver.Chrome(options=chrome_options)

    ### BROWSERSTACK ###

    bs_user = 'habeebkassim_XKky1W'
    bs_key = 'wJnEA55jyn9dqK2ccu44'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    bstack_options = {
        'deviceName': 'Samsung Galaxy S20 Ultra',
        'osVersion': '10.0',  # Confirmed supported version for S20 Ultra
        'realMobile': 'true',
        'projectName': 'Internship Project',
        'buildName': 'BDD Mobile Web Tests',
        'sessionName': 'Test on Samsung S20 Ultra',
        'debug': True,
        'networkLogs': True,
        'interactiveDebugging': True
    }

    # Setup Chrome mobile browser on Android
    options = Options()
    options.set_capability('browserName', 'Chrome')
    options.set_capability('platformName', 'Android')
    options.set_capability('bstack:options', bstack_options)

    # Initialize WebDriver
    context.driver = webdriver.Remote(command_executor=url, options=options)

    # bstack_options = {
   #      "os" : "Windows",
   #      "osVersion" : "11",
   #      'browserName': 'Edge',
   #      'sessionName': scenario_name,
   #  }
   #  options.set_capability('bstack:options', bstack_options)
   #  context.driver = webdriver.Remote(command_executor=url, options=options)

   # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 15)
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
