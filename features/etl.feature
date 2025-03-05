Feature: Data preparation (ETL) Feature
  
  
  Scenario: ETL Training Data
    # In the real work, we don't need to create synthetic data.
    Given The '100' records of synthetic data is generated with the columns name and age
    # the reason of using two "Given" to create the synthetic data is to reuse the python code in the batch infer feature
    And Adding the inferece target column frauld
    # In the real work, We deploy the image to ECS and run it.
    When I run ETL for training data to generate a csv file 'training_data.csv'
    Then I should see a csv file named: 'training_data.csv' is generated
    And The file should have '100' records
    And There are new column 'Gender' is created and the value is in ('0,1,2')
    And The age shoule less than '150' and more than '0'.
