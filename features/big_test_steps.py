from lettuce import *

@step('I have an account')
def has_account(step):
    # check if there is an account with the username
    pass

@step("I'm at least an observer")
def user_type(step):
    # check account type
    # return True if is an [observer]
    pass

@step("I'm logged in uberVU")
def is_logged_in(step):
    # Check that the main menu is present
    pass

@step('I can add new streams:')
def add_streams(step):
    # Check if user has streams left.
    pass

@step('I click "(.*)"')
def click_to_add_stream(step, element):
    # element_selector = get_selector(element)
    # element_by = get_by(element_selector)
    # common.get(element_by, element_selector).click()
    pass

@step('I fill expression')
def fill(step):
    # element_selector = get_selector(element)
    # element_by = get_by(element_selector)
    # common.get(element_by, element_selector).sendkeys(value)
    assert step.hashes.first['col1'] == 'company', \
            "Mesaj"
    assert step.hashes.last['col2'] == 'ceva', \
            "Mesaj2"

@step('But I don\'t select "(.*)"')
def select(step, element):
    pass

@step('I see the "(.*)"')
def is_present(step, element):
    # element_selector = get_selector(element)
    # element_by = get_by(element_selector)
    # common.is_present(element_by, element_selector)
    pass
