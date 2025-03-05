Feature: Realtime Inference Feature
  # The function under backgound will be used in every scenario of this feature.
  Background: Realtime inference setting
    Given the endpoint base url is 'https://petstore.swagger.io/v2',and the model context path is '/pet'
  
  # In the real work, we send the raw data to API Gateway, the data will be ETLed and the inference result will be returned.
  Scenario Outline: Send a request to the model for realtime inference
    # If the API Gateway needs the authentication, we can use a "secret" header to pass the token.
    When I send the <category_name>, <name>, <status> to the model
    Then The endpoint should return the response with status code '200'
    And The response should have the key 'id', and it is a number
    Examples:
        | category_name | name | status |
        | cat  | meow  | available  |
        | dog  | woof  | pending  |
        | fish  | red  | sold  |