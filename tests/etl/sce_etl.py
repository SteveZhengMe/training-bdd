from behave import given, when, then
import os
import csv
from src.etl import Etl
import random


@given(
    "The '{data_row_count}' records of synthetic data is generated with the columns name,age and frauld"
)
def prepare_testing_data(context, data_row_count):
    # Generate synthetic data and save to a CSV file
    context.csv_file = "synthetic_data.csv"
    data_row_count = int(data_row_count)
    with open(context.csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "frauld"])
        for i in range(data_row_count):
            writer.writerow(
                [f"name_{i}", random.randint(-10, 200), random.choice([0, 1])]
            )


@when("I run ETL for training data to generate a csv file '{generated_file_name}'")
def invoke_etl_class(context, generated_file_name):
    context.etl = Etl(context.csv_file)
    context.etl.derive_gender()
    context.etl.fix_age()
    context.output_file = generated_file_name
    with open(context.output_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(context.etl.data)


@then("I should see a csv file named: '{generated_file_name}' is generated")
def check_if_file_generated(context, generated_file_name):
    assert os.path.exists(generated_file_name)


@then("The file should have '{generated_row_count}' records")
def check_row_count(context, generated_row_count):
    generated_row_count = int(generated_row_count)
    with open(context.output_file, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert len(rows) == generated_row_count + 1  # Including header row


@then(
    "There are new column '{column_name}' is created and the value is in ('{value_choices}')"
)
def check_gender_column(context, column_name, value_choices):
    value_choices = [int(v) for v in value_choices.split(",")]
    with open(context.output_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        assert column_name in header
        gender_index = header.index(column_name)
        for row in reader:
            assert int(row[gender_index]) in value_choices


@then("The age shoule less than '{max_age}' and more than '{min_age}'.")
def validate_age(context, max_age, min_age):
    max_age = int(max_age)
    min_age = int(min_age)
    with open(context.output_file, "r") as f:
        reader = csv.reader(f)
        header = next(reader)
        age_index = header.index("age")
        for row in reader:
            age = int(row[age_index])
            assert min_age <= age <= max_age
