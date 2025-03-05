import os
import requests
import logging

from behave import given, when, then
from src.batch_infer import BatchInfer


@given(
    "the endpoint base url is '{endpoint_base_url}',and the model context path is '{context_path}'"
)
def configure_endpoint(context, endpoint_base_url, context_path):
    context.endpoint_url = endpoint_base_url + context_path + "/"


@when("I send the {category_name}, {name}, {status} to the model")
def send_data_to_model(context, category_name, name, status):
    request_body = {"category": {"name": category_name}, "name": name, "status": status}
    headers = {"accept": "application/json", "Content-Type": "application/json"}
    # In the real work, send the REST request to API Gateway
    context.response = requests.post(
        context.endpoint_url, json=request_body, headers=headers
    )
    logging.debug(context.response.url)


@then("The endpoint should return the response with status code '{http_status_code}'")
def check_response_status_code(context, http_status_code):
    assert context.response.status_code == int(http_status_code)


@then("The response should have the key '{new_id}', and it is a number")
def validate_new_id(context, new_id):
    response_data = context.response.json()
    assert new_id in response_data
    assert isinstance(response_data[new_id], int)
