@echo off

:: Navigate outside of the project-vote4us directory
cd ..

:: Create virtual environment
python -m venv .venv

:: Activate virtual environment
call .venv\Scripts\activate

:: Install libraries
:: We can probably get rid of the install for opencv-contrib-python
pip install opencv-contrib-python
pip install cvlib
pip install tensorflow
pip install ultralytics

:: run the python files for setting up .yaml file
cd project-vote4us
python MLTest\setup_ML.py

echo Virtual Environment setup completed.