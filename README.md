# BDD Training Matirials

## Introduction

The repository is for Behaviour Driven Development (BDD) training. The BDD scenarios should cover the below features(requirements):

- ETL process: Assume that we have a source file (csv) with 100 records. The columns are: name, age (0~150), frauld (0,1). The ETL requirement:
  - Derive a new column "gender" with random value of (0,1,2).
  - Change the age to the average value if it out of range.
- ML Batch Inference: Assume that we have a model that can infer "frauld", and we have a csv file with 120 records. The columns are: name, age. The inference requirement:
  - ETL the data before inference based on the ETL requirement.
  - Inference the "frauld" value for each record.
- ML Realtime Inference: We don't have a realtime ML inference server, but the realtime inference is just about sending the REST request. We will use the famous "Pet Store" API to simulate the realtime inference. The base url is <https://petstore.swagger.io/v2/>.

## BDD Description

### 1. ETL Feature

ETL feature has one scenario that covers the two requirements. See the file `features/etl.feature`.

### 2. ML Batch Feature

ML Batch feature has two scenarios, ETL the data and "send to inference model". See the file `features/ml_batch.feature`.

### 3. Realtime Batch Feature

Realtime Batch feature has two scenarios, send GET request and send POST request. See the file `features/ml_realtime.feature`.

## Folder Structure

- features: Contains feature files for (BDD) testing. One feature one file.
  - steps: The default steps files (implementation python code) are under steps, I move them to tests folder. The `__init__.py` is for import them dynamically.
- src: Contains project source code. They are mock code to simulate the real project.
- tests: Includes BDD step python code. Each feature is a folder.
  - example: Provides the simple example of BDD. **You want to start from here.**
  - etl: Contains BDD test scripts of `etl.feature`.
  - batch_infer: Contains BDD test scripts of `batch_infer.feature`.
  - realtime_infer: Contains BDD test scripts of `realtime_infer.feature`.
  
## Run BDD Test

The project libraries are managed by `[poetry](https://python-poetry.org/)`. You can run the BDD test by following the below steps:

Step 1. Install `poetry`:

- `curl -sSL https://install.python-poetry.org | python3 -`

Step 2. Install the dependencies:

- `poetry install`

Step 3. Run the BDD test:

- `poetry run behave features`
- Or `./run.sh`

The test results will be shown in the console.
