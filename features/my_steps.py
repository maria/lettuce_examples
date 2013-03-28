from lettuce import *

@step('I have the number (\d+)')
def i_have_number(step, number):
    world.number = int(number)

@step('I compute his factorial')
def compute_factorial(step):
   world.factorial = factorial(world.number)

@step('I get the number (\d+)')
def get_the_number(step, factorial):
    assert (world.factorial == factorial,
        "They are not equal")

def factorial(n):
    if n == 1 or n == 0:
        return 1
    elif n > 1:
        fact = factorial(n-1) + factorial(n-2)
        return fact
    else:
        return 0
