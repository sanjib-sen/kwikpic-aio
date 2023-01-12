from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np


def add_text_watermark(image_path, text, size=11, directory="", text_position="bottom-right"):
    if size == 31:
        size = 31.05
    image = Image.open(image_path)
    w, h = image.size
    watermark_image = image.copy()
    draw = ImageDraw.Draw(watermark_image)
    fontsize = int(max(w, h)/(31-size))
    font = ImageFont.truetype("arial.ttf", fontsize)

    pos = text_position
    if pos == "bottom-right":
        position = (int(w-fontsize*len(text)*0.5), int(h-fontsize*1.5))
    elif pos == "bottom-left":
        position = (0, int(h-fontsize*1.5))
    elif pos == "top-left":
        position = (0, 0)
    elif pos == "top-right":
        position = (int(w-fontsize*len(text)*0.5), 0)

    draw.text(position, text, fill=(255, 255, 255), font=font)
    file_name = image_path.split("/")[-1]
    new_path = None
    if directory == "" or directory[-1] == "/" or directory[-1] == "\\":
        new_path = directory+file_name
    else:
        new_path = directory+"/"+file_name
    watermark_image.save(new_path)


def add_image_watermark(destination_image_path, watermark_image_path, size=11, directory="", watermark_position="top-right"):
    if size == 19:
        size = 19.05
    copied_image = Image.open(destination_image_path)
    w, h = copied_image.size
    size = (w/(19-size), h/(19-size))
    crop_image = Image.open(watermark_image_path)
    crop_image.thumbnail(size)

    pos = watermark_position
    if pos == "bottom-right":
        position = (int(w-size[0]), int(h-size[1]))
    elif pos == "bottom-left":
        position = (0, int(h-size[1]))
    elif pos == "top-left":
        position = (0, 0)
    elif pos == "top-right":
        position = (int(w-size[0]), 0)

    copied_image.paste(crop_image, position)

    file_name = destination_image_path.split("/")[-1]
    new_path = None
    if directory == "" or directory[-1] == "/" or directory[-1] == "\\":
        new_path = directory+file_name
    else:
        new_path = directory+"/"+file_name
    copied_image.save(new_path)


# add_text_watermark("favicon-512x512.png", "sanjibsen",
#                    directory="venv\\", size=15)
# add_image_watermark("favicon-512x512.png", "cover.jpg",
#                     directory="venv\\", size=7, watermark_position="bottom-left")
