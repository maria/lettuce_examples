from lettuce import *

@step('I have the number (\d+)')
def i_have_number(step, number):
    world.number = int(number)

@step('I compute his factorial')
def compute_his_factorial(step):
    world.factorial = compute_factorial(world.number)

@step('I get the number (\d+)')
def get_the_number(step, given_factorial):
    assert world.factorial == int(given_factorial), \
        "Got %s" % world.factorial

@step('I have the numbers (\d+), (\d+)')
def i_have_numbers(step, a, b):
    world.a = int(a)
    world.b = int(b)

@step('I compute addition')
def compute_addition(step):
    world.addition = add_numbers(world.a, world.b)

@step('I get the sum (\d+)')
def get_the_number(step, sum):
    assert world.addition == int(sum), \
        "Got %s" % world.addition

def add_numbers(a, b):
    return a + b

def compute_factorial(n):
    if n <= 1:
        return 1
    elif n > 1:
        fact = compute_factorial(n-1) * n
        return fact
