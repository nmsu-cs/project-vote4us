@echo off

:: Navigate outside of the project-vote4us directory
cd ..

:: Create virtual environment
::python3 -m venv .venv        :: (for mac)
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
python project-vote4us\MLTest\setup_ML.py

echo Virtual Environment setup completed.