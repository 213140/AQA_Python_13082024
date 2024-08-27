# Given list of tuples (name, surname, age, profession, City location)
import deepcopyall

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

# 1 - Add your new record o the beginning of the given list
people_records.insert(0, ('Andzej', 'Mackevic', 29, 'Engineer', 'Czestochowa'))

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
copy_of_people_records = deepcopyall.deepcopy(people_records)
element_1 = list(copy_of_people_records[1])
element_5 = list(copy_of_people_records[5])
people_records[1] = element_5
people_records[5] = element_1
print(people_records)

# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
index_tuple = (6, 10, 13)
for pos_index in index_tuple:
  if people_records[pos_index][2] >= 30:
    print(f"People with index {pos_index} is {people_records[pos_index][2]} "
          f"years old, it`s more than or eqal 30")
  else:
    print(f"People with index {pos_index} is {people_records[pos_index][2]} "
          f"years old, it`s less than 30")
