Feature: ETL Feature

  Scenario: ETL Training Data
    Given The '100' records of synthetic data is generated with the columns name,age and frauld
    When I run ETL for training data to generate a csv file 'training_data.csv'
    Then I should see a csv file named: 'training_data.csv' is generated
    Then The file should have '100' records
    Then There are new column 'Gender' is created and the value is in ('0,1,2')
    Then The age shoule less than '150' and more than '0'.
