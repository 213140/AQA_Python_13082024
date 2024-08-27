adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
list_of_strings = adwentures_of_tom_sawer.split()
solved_list_of_strings = []
for word in list_of_strings:
    solved_list_of_strings.append(word.strip())
adwentures_of_tom_sawer = " ".join(solved_list_of_strings)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print(f"Number of \"h\" letter in description: {adwentures_of_tom_sawer.count("h")}")


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
list_of_words = adwentures_of_tom_sawer.split()
number_of_title_words = 0
for word in list_of_words:
    if word.istitle():
        number_of_title_words += 1
print(f"Number of title word in description: {number_of_title_words}")

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
print(f"""Second found 'Tom' word in the description is located 
on possition: {adwentures_of_tom_sawer.find("Tom", 
                                            adwentures_of_tom_sawer.find("Tom") + 1)}""")

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split(". ")

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(f"""Fourth sentence fro mdescription in lowercase: 
{adwentures_of_tom_sawer_sentences[3].lower()}""")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
for sentence in adwentures_of_tom_sawer_sentences:
    if sentence.startswith("By the time"):
        print(f""""{sentence}" sentence starts with 'By the time'""")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print(f"""Last sentence contains 
{len(((adwentures_of_tom_sawer_sentences[len(adwentures_of_tom_sawer_sentences) 
                                         - 1]).split()))} words""")
