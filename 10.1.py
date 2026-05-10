# 10.1.py
from PIL import Image

img = Image.open("postcard.jpg")
cropped = img.crop((0, 0, img.width, img.height - 100))
cropped.save("cropped_postcard.jpg")
print("Обрезанное изображение сохранено")
