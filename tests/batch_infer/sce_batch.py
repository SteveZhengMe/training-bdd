import os
from behave import given, when, then
from src.batch_infer import BatchInfer


@given("Seeing the data '{source_file}' is ready")
def check_source_data_ready(context, source_file):
    # check if the source data file is exist
    context.source_data = source_file
    assert os.path.exists(source_file)


@when("I send the data to the model to generate the result file '{target_file}'")
def perform_infer(context, target_file):
    # initialize the BatchInfer class and call the infer method
    context.target_file = target_file
    model = BatchInfer(context.source_data)
    model.infer(context.target_file)


@then("I should see the inference result file named: '{target_file}' is generated")
def file_exist(context, target_file):
    # check if the target file is generated
    assert os.path.exists(target_file)


@then("'{source}' should have the same records count as '{target}'")
def check_row_count(context, source, target):
    # check if the source file and target file have the same records count
    with open(source, "r") as sf:
        reader = sf.readlines()
        source_row_count = len(reader) - 1
    with open(target, "r") as tf:
        reader = tf.readlines()
        target_row_count = len(reader) - 1
    assert source_row_count == target_row_count


@then(
    "There is a new column '{target_column_name}' is created and the value is in ('{expected_values}')"
)
def check_infer_target_column(context, target_column_name, expected_values):
    # check if the target column is created and the value is in the expected values
    expected_values = [int(v) for v in expected_values.split(",")]
    with open(context.target_file, "r") as f:
        reader = f.readlines()
        header = reader[0].strip().split(",")
        assert target_column_name in header
        target_column_index = header.index(target_column_name)
        for row in reader[1:]:
            row = row.strip().split(",")
            assert int(row[target_column_index]) in expected_values
