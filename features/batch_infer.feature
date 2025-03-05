Feature: Batch Inference Feature

  # We don't need two scenarios in the real work. Because the ETL image and inference image are orchestrated by the StepFunctions.
  # So in the real work, we will use boto3 to trigger the StepFunctions, and check the status of the StepFunctions and the output data file.
  Scenario: Data preparation (ETL)
    # We don't need create synthetic data in the real work.
    Given The '120' records of synthetic data is generated with the columns name and age
    # Notice that there is no python code for the scenario, because we are reusing the code for etl.feature
    When I run ETL for training data to generate a csv file 'infer_data.csv'
    Then I should see a csv file named: 'infer_data.csv' is generated
    And The file should have '120' records
    And There are new column 'Gender' is created and the value is in ('0,1,2')
    And The age shoule less than '150' and more than '0'.

  Scenario: Invoke the model for batch inference
    Given Seeing the data 'infer_data.csv' is ready
    When I send the data to the model to generate the result file 'infer_result.csv'
    Then I should see the inference result file named: 'infer_result.csv' is generated
    And 'infer_result.csv' should have the same records count as 'infer_data.csv'
    And There is a new column 'target' is created and the value is in ('0,1')
