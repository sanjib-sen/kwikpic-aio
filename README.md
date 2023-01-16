# Kwikpic All In One

## Instruction

### Windows

```sh
python -m venv venv && ./venv/Scripts/activate && pip install pillow opencv-python pyqt6 pyinstaller && python main.py
```

### Mac

```sh
python3 -m venv venv && source venv/bin/activate && pip install pillow opencv-python pyqt6 pyinstaller && python3 main.py
```

## Screenshot

![image](screenshot.jpeg)

## BUILD

### Windows Build

```ps
pyinstaller --onefile --name Kwikpic --noconsole --clean --icon="icon.ico" --add-data "logo/logo.png;."  main.py --paths="venv\Lib\site-packages\cv2"
```

### Mac Build

```sh
pyinstaller --noconsole --name Kwikpic --windowed --clean --onedir --add-data "logo/logo.png:." --icon icon.ico main.py
```
