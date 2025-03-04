from behave import given, when, then
from example import Calculator


@given("I have a number {number}")
def initial_first_number(context, number):
    # put the number 1 in the context
    context.number = int(number)


@when("I add {another} to the number")
def test_calculator_class_in_example(context, another):
    c = Calculator()
    context.number = c.add(context.number, int(another))


@then("I will get {result}")
def check_result(context, result):
    assert context.number == int(result)
