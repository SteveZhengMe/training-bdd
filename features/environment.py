import logging

# Please note: the below code is not tested in any AWS account.


# import boto3
# from botocore.config import Config
# from behave.model_core import Status

# Create CloudWatch client
# config = Config(
#     region_name="us-east-1",
#     signature_version="v4",
#     retries={"max_attempts": 10, "mode": "standard"},
# )
# cloudwatch = boto3.client("cloudwatch", config=config)


# Put custom metrics
def write_metric(test_name, value):
    # print(f"{test_name}: {value}")
    # cloudwatch.put_metric_data(
    #     MetricData=[
    #         {
    #             "MetricName": "FAILED_TESTS",
    #             "Dimensions": [
    #                 {"Name": "TEST_NAME", "Value": test_name},
    #             ],
    #             "Unit": "None",
    #             "Value": value,
    #         },
    #     ],
    #     Namespace="TESTS",
    # )
    pass


def after_scenario(context, scenario):
    # if scenario.status == Status.passed:
    #     value = 0.1
    # elif scenario.status == Status.failed:
    #     value = 1.0
    # if value:
    #     write_metric(scenario.name, value)

    logging.info(f"{scenario}>>> Implement me to send metrics to AWS CloudWatch!")
