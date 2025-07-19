from behave import given, when, then
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from time import sleep




@given('open the main page')
def step_open_main_page(context):
    context.driver.get("https://soft.reelly.io")
    context.login_page = LoginPage(context.driver)
    context.settings_page = SettingsPage(context.driver)

@when('user logs in with valid credentials')
def step_login(context):
    context.login_page.login("your_email@example.com", "your_password")

@when('user navigates to the settings page')
def step_navigate_to_settings(context):
    context.settings_page.go_to_settings()


@then('settings page should be displayed')
def step_verify_settings_page(context):
    assert context.settings_page.is_settings_page_open(), "Settings page is not open"

@then('settings page should have 18 options')
def step_verify_option_count(context):
    count = context.settings_page.count_settings_items()
    assert count == 18, f"Expected 18 options, but found {count}"



@then('the "{button_text}" button should be visible')
def step_verify_connect_company_button(context, button_text):
    assert context.settings_page.is_connect_company_visible(), f'"{button_text}" button is not visible'