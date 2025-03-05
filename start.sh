#!/bin/bash

# 1. install poetry
if ! command -v poetry &> /dev/null
then
    echo "Installing poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

# 2. Install default-jre-headless (the dependency of allure)
if ! dpkg -s default-jre-headless &> /dev/null
then
    echo "Installing default-jre-headless..."
    sudo apt-get update
    sudo apt-get install -y default-jre-headless
fi

# 3. Install allure (Beautify the BDD test report)
if ! command -v allure &> /dev/null
then
    echo "Installing allure..."
    wget https://github.com/allure-framework/allure2/releases/download/2.33.0/allure_2.33.0-1_all.deb
    sudo dpkg -i allure_2.33.0-1_all.deb
    sudo apt-get install -f -y
    rm allure_2.33.0-1_all.deb
fi

# 4. Install Python libraries dependencies
echo "Installing dependencies with poetry..."
poetry install --no-root

# 5. Run All BDD tests
echo "Running behave tests..."
poetry run behave -f allure_behave.formatter:AllureFormatter -o reports_data features

# 6. Generate allure reports
echo "Generating allure report..."
allure generate reports_data/ -o reports/ --clean

echo "All done! Open reports/index.html in your browser to view the report."
