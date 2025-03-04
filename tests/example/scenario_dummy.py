from behave import given, when, then
import example


@given("I have a number 1")
def initial_first_number(context):
    # put the number 1 in the context
    context.number = 1


@when("I add 1 to the number")
def test_calculator_class_in_example(context):
    c = example.Calculator()
    context.number = c.add(context.number, 1)


@then("I get 2")
def check_result(context):
    assert context.number == 2
