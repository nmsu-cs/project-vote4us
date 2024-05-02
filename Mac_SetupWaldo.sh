#!/bin/bash

# Navigate outside of the project-vote4us directory
cd ..

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install libraries
pip install opencv-contrib-python
pip install cvlib
pip install tensorflow
pip install ultralytics

# Run the Python files for setting up .yaml file
cd project-vote4us
python project-vote4us/MLTest/setup_ML.py

echo "Virtual Environment setup completed."