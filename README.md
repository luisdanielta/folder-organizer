python3 -m pip install -r requirements.txt

pip freeze > requirements.txt

pyinstaller --clean -w --onefile main.py