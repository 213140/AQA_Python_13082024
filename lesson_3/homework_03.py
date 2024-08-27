#Initial string
#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = """
'"Would you tell me, please, which way I ought to go from here?"\n
"That depends a good deal on where you want to get to," said the Cat.\n
"I don't much care where ——" said Alice.\n
"Then it doesn't matter which way you go," said the Cat.\n
"—— so long as I get somewhere," Alice added as an explanation.\n
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'"""

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
for character in alice_in_wonderland:
    if character == "'":
        print(character)

# task 03 == Виведіть змінну alice_in_wonderland на
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
print(f"Black and Azov seas cover {black_sea_area + azov_sea_area} km2")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
all_products = 375291
warehouse_1_and_2 = 250449
warehouse_2_and_3 = 222950
warehouse_1 = all_products - warehouse_2_and_3
print(f"Warehouse 1 contains {warehouse_1} products")
warehouse_3 = all_products - warehouse_1_and_2
print(f"Warehouse 3 contains {warehouse_3} products")
warehouse_2 = all_products - warehouse_1 - warehouse_3
print(f"Warehouse 2 contains {warehouse_2} products")

"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
price_of_computer = 18 * 1179
print(f"Price of computer is: {price_of_computer}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print(f"rest of 8019 : 8 is: {8019%8}")
print(f"rest of 9907 : 9 is: {9907%9}")
print(f"rest of 2789 : 5 is: {2789%5}")
print(f"rest of 7248 : 6 is: {7248%6}")
print(f"rest of 7128 : 5 is: {7128%5}")
print(f"rest of 19224 : 9 is: {19224%9}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
price_list = {
    "big_pizza" : 274,
    "mid_pizza" : 218,
    "juice" : 35,
    "cake" : 350,
    "water" : 21
}
print(f"For all shoping Irinka will need {price_list["big_pizza"] * 4 + price_list["mid_pizza"] * 2 + price_list["juice"] * 4 + price_list["cake"] + price_list["water"] * 3} grivns")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
igor_photos = 232
required_pages = igor_photos // 8
additional_page = igor_photos % 8 > 0
print(f"Igor will need {required_pages + additional_page} pages album to put all photos inside")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
petrol_consuption = 9
bank_capacity = 48
how_many_liters_are_needed = int(distance / 100 * petrol_consuption)
print(f"For all tripp will be needed {how_many_liters_are_needed} liters of bensin")
print(f"Familly will need {int(how_many_liters_are_needed // bank_capacity)} stops during that trip")