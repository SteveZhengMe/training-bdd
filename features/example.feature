Feature: My feature
  # you can add description here. The description will be in the Allure report and other output.
  This is a description of my feature. It won't be used in the python code.
  If you want to refer it, use Feature.description in your code.
  Suggest to use the epic user story format.
  
  # No parameter
  Scenario: Dummy calcultor
    This is the description of the scenario. It won't be used in the python code.
    If you want to refer it, use Scenario.description in your code.
    Suggest to use the user story format.
    Given I have a number 1
    When I add 1 to the number
    Then I get 2

  # in-line parameter. Behave use regix to parse the parameter, the paremter always string type.
  Scenario: Parameter calcultor
    Given I have a number 10
    When I add 1 to the number
    Then I will get 11
  
  # If you have many group of parameters, you can use the Examples with <> to define.
  Scenario Outline: Group Parameter calcultor
    Given I have numbers <first_number>
    When I add <another_number> to the first numbers
    Then I get the result: <the_result>
    Examples:
    | first_number | another_number | the_result |
    | 100            | 1              | 101          |
    | 1000           | 10              | 1010         |
    | 10000           | 100              | 10100         |
