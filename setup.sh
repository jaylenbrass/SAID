#!/bin/bash

echo "Setting up SAID..."

if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed."
    echo "Please install Python 3 from https://www.python.org/downloads/"
    exit 1
fi

python3 -m venv .venv

source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Setup complete."
echo "Run SAID with: ./run.sh"