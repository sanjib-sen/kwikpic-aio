# Kwikpic All In One

## Instruction

## Windows
```ps
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
python main.py
```

## Mac and Linux
```ps
python3 -m venv venv
./venv/bin/activate
pip install -r requirements.txt
python3 main.py
```


## Screenshot

![image](screenshot.jpeg)

## BUILD

### Windows

```ps
pyinstaller --onefile --name Kwikpic --noconsole --clean --icon="icon.ico" --add-data "logo/logo.png;."  main.py --paths="venv\Lib\site-packages\cv2"
```

### Mac

```sh
pyinstaller --noconsole --name Kwikpic --windowed --clean --onedir --add-data "logo/logo.png:." --icon icon.ico main.py
```
