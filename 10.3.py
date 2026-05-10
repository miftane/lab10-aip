# 10.3.py
from PIL import Image, ImageDraw, ImageFont

postcards = {
    "Новый год": "new_year.jpg",
    "8 марта": "march_8.jpg",
    "23 февраля": "feb_23.jpg",
    "День рождения": "birthday.jpg"
}

print("Доступные праздники:")
for holiday in postcards.keys():
    print(f"- {holiday}")

holiday_choice = input("К какому празднику нужна открытка? ")
name = input("Введите имя поздравляемого: ")

if holiday_choice in postcards:
    try:
        img = Image.open(postcards[holiday_choice])
        draw = ImageDraw.Draw(img)
        
        try:
            font = ImageFont.truetype("arialbd.ttf", 60)
        except:
            try:
                font = ImageFont.truetype("arial.ttf", 60)
            except:
                font = ImageFont.load_default()
        
        text = f"{name}, поздравляю!"
        
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        x = (img.width - text_width) // 2
        y = 50  
        
        draw.text((x, y), text, fill="blue", font=font)
        
        output_filename = f"greeting_{name}_{holiday_choice}.png"
        img.save(output_filename)
        print(f"Открытка сохранена как {output_filename}")
        img.show()
        
    except FileNotFoundError:
        print("Файл с открыткой не найден")
else:
    print("Праздник не найден")
