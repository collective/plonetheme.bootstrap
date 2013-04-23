*** Settings ***
Suite Setup     Suite Setup
Suite Teardown  Suite Teardown
Variables       plonetheme/bootstrap/tests/robot/variables.py
Library         Selenium2Library  timeout=${SELENIUM_TIMEOUT}  implicit_wait=${SELENIUM_IMPLICIT_WAIT}
Resource        plone/app/robotframework/selenium.robot
Resource        plonetheme/bootstrap/tests/robot/keywords.txt

*** Test Cases ***

Test layout
  Given a Plone site skinned with this product
  When I go to the home page
  I can see a beatiful layout
  Capture Page Screenshot  filename=homepage.png

*** Keywords ***
a Plone site skinned with this product
  Comment  the test fixture takes care of this

I go to the home page
  go to  ${PLONE_URL}

I can see a beatiful layout
  Comment  some human eyes should check this
