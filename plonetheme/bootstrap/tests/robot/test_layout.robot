*** Settings ***
Suite Setup     Suite Setup
Suite Teardown  Suite Teardown
Variables       plonetheme/bootstrap/tests/robot/variables.py
Library         Selenium2Library  timeout=${SELENIUM_TIMEOUT}  implicit_wait=${SELENIUM_IMPLICIT_WAIT}
Resource        plone/app/robotframework/keywords.robot
Resource        plone/app/robotframework/selenium.robot

Library         Remote  ${PLONE_URL}/RobotRemote

*** Test Cases ***

Test layout for Manager
  Given a Plone site skinned with this product
  When I go to the home page as  Manager
  I can see a beatiful layout named  manager_homepage.png
  Error log is empty

Test layout for Anonymous
  Given a Plone site skinned with this product
  When I go to the home page as Anonymous
  I can see a beatiful layout named  anonymous_homepage.png
  Error log is empty


*** Keywords ***
a Plone site skinned with this product
  Comment  the test fixture takes care of this

I go to the home page
  go to  ${PLONE_URL}

I can see a beatiful layout named
  [Arguments]  ${filename}
  Comment  some human eyes should check this: take a screenshot
  Capture Page Screenshot  filename=${filename}

I go to the home page as
  [Arguments]  ${role}
  Enable autologin as  ${role}
  go to  ${PLONE_URL}

I go to the home page as Anonymous
  Disable autologin
  go to  ${PLONE_URL}

Suite Setup
  Open browser  ${PLONE_URL}  browser=${BROWSER}  remote_url=${REMOTE_URL}  desired_capabilities=${DESIRED_CAPABILITIES}

Suite Teardown
  Close All Browsers
