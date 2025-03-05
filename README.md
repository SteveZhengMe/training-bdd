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

## Repository Description

In the demo, there are four features:

### 1. Example

There are three scenarios in it. The example shows how to write the BDD test scripts and how to implement the steps. You can start from here after reading the basic BDD concepts ([Here](https://behave.readthedocs.io/en/stable/philosophy.html) & [Here](https://cucumber.io/docs/gherkin/reference)) and behave framework tutorial ([Here](https://behave.readthedocs.io/en/stable/tutorial.html)).

### 2. ETL Feature

ETL feature has one scenario that covers the two requirements. See the file `features/etl.feature`.

### 3. ML Batch Feature

ML Batch feature has two scenarios, ETL the data and "send to inference model". See the file `features/ml_batch.feature`.

### 4. Realtime Batch Feature

Realtime Batch feature has one scenarios, send POST request. See the file `features/ml_realtime.feature`.

## Folder Structure

- features: Contains feature files for (BDD) testing. One feature one file.
  - steps: The default steps files (implementation python code) are under steps, I move them to tests folder. The `__init__.py` is for import them dynamically.
- src: Contains project source code. They are mock code to simulate the real project.
- tests: Includes BDD step python code. Each feature is a folder.
  - example: Provides the simple example of BDD. **You want to start from here.**
  - etl: Contains BDD test scripts of `etl.feature`.
  - batch_infer: Contains BDD test scripts of `batch_infer.feature`.
  - realtime_infer: Contains BDD test scripts of `realtime_infer.feature`.
  
## Quick Start

Step 1. Clone the repository

- `git clone https://github.com/SteveZhengMe/training-bdd`

Step 2. Run all-in-one script

- `./start.sh`

Step 3. Open `index.html` to check the reports under `reports` folder.

## Continue Developing

After you run `start.sh`, your development environment is all set. Here is some key items:

- The project libraries are managed by `[poetry](https://python-poetry.org/)`. WHen you want to run python, you need to use `poetry run python ...`. Poetry will catch your libraroes.
- If you want to run all features, like `run.sh` does, you can use `poetry run behave features`.
- If you want to run a specific feature, you can use `poetry run behave features/etl.feature`.
- When you run the above command, the test results will be shown in the console.
- To see a better report, you want the help from [Allure](https://allurereport.org/). Allure is not the key tools, we use it only for the demo purpose. Or we want to have a human friendly report in production. (Don't put much time on Allure)
- Send the BDD report to CloudWatch is sessential in production. `environment.py` under `./features` folder can help. Please note, it is not implemented yet. So you can see it in the log.log file.
- Any further questions, please contact me. You know where I am.
