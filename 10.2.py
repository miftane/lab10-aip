# 10.2.py
from PIL import Image

postcards = {
    "Новый год": "new_year.jpg",
    "8 марта": "march_8.jpg",
    "23 февраля": "feb_23.jpg",
    "День рождения": "birthday.jpg"
}

print("Доступные праздники:")
for holiday in postcards.keys():
    print(f"- {holiday}")

choice = input("К какому празднику нужна открытка? ")

if choice in postcards:
    try:
        img = Image.open(postcards[choice])
        img.show()
    except FileNotFoundError:
        print("Файл с открыткой не найден")
else:
    print("Праздник не найден в списке")
