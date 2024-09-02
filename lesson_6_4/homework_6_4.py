list = [1, 4, 57, 79, 6, 9, 12, 7, 9, 11, 100 ]
list2 = []

for item in list:
    if item % 2 == 0:
        list2.append((item))

print(f"Sum of all even numbers is {sum(list2)}")