Feature: Realtime Inference Feature
  Background: Realtime inference setting
    Given the endpoint base url is 'https://petstore.swagger.io/v2',and the model context path is '/pet'
  
  Scenario Outline: Send a request to the model for realtime inference
    When I send the <category_name>, <name>, <status> to the model
    Then The endpoint should return the response with status code '200'
    And The response should have the key 'id', and it is a number
    Examples:
        | category_name | name | status |
        | cat  | meow  | available  |
        | dog  | woof  | pending  |
        | fish  | red  | sold  |