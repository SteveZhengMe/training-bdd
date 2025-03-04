Feature: My feature
  This is a description of my feature. It won't be used in the python code.
  If you want to refer it, use Feature.description in your code.
  Suggest to use the epic user story format.
  
  Scenario: Dummy calcultor
    This is the description of the scenario. It won't be used in the python code.
    If you want to refer it, use Scenario.description in your code.
    Suggest to use the user story format.
    Given I have a number 1
    When I add 1 to the number
    Then I get 2

  Scenario: Parameter calcultor
    Given I have a number 10
    When I add 1 to the number
    Then I will get 11
  
  Scenario Outline: Group Parameter calcultor
    Given I have numbers <first_number>
    When I add <another_number> to the first numbers
    Then I get the result: <the_result>
    Examples:
    | first_number | another_number | the_result |
    | 100            | 1              | 101          |
    | 1000           | 10              | 1010         |
    | 10000           | 100              | 10100         |
