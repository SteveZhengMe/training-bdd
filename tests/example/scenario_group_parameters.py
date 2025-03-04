from behave import given, when, then
from example import Calculator


@given("I have numbers {first_number}")
def initial_first_number(context, first_number):
    # put the number 1 in the context
    context.number = int(first_number)


@when("I add {another_number} to the first numbers")
def test_calculator_class_in_example(context, another_number):
    c = Calculator()
    context.number = c.add(context.number, int(another_number))


@then("I get the result: {the_result}")
def check_result(context, the_result):
    assert context.number == int(the_result)
