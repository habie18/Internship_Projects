from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)

    #chrome_options = Options()
    #chrome_options.add_argument("--headless")  # run in headless mode
    #chrome_options.add_argument("--window-size=1920,1080")  # avoid layout issues
    #chrome_options.add_argument("--disable-gpu")  # optional for Windows
    #chrome_options.add_argument("--no-sandbox")  # recommended for Linux CI

   # context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()

    #firefox_options = FirefoxOptions()
    #firefox_options.headless = True  # enable headless mode

    # Optional settings
    #firefox_options.add_argument("--width=1920")
    #firefox_options.add_argument("--height=1080")

   # context.driver = webdriver.Firefox(options=firefox_options)

def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
