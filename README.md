# Minimal Python project template
## Setup
To set up the project environment, run:
```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
## Adding dependencies
To add a new dependency:
```
source env/bin/activate
pip install <package-name>
pip freeze > requirements.txt
```
## Running the project
To run the project:
```
source env/bin/activate
python app/main.py
```
Remember to deactivate the virtual environment when you're done with:
```
deactivate
```
