# Created by habeeb at 7/17/2025
Feature: Settings and page validation

  Scenario: User can go to settings and see the right number of UI elements
    Given open the main page
    When User logs in with valid credentials
    And User navigates to the settings page
    Then Settings page should be displayed
    And Settings page should have 13 options
    And the "Connect the Company" button should be visible