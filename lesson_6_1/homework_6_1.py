#Receive and string from user
entered_string = input("Please enter some string:")
print(f"User entered string: {entered_string}")

#Cretae empty list and fulfill by single characters fro mstring
characters_list = []
characters_list = entered_string[::1]

#Create Set with single characters
characters_set = set(characters_list)
print(f"Final set: \n {characters_set}")

#Check if unique characters quantity in the string is more than 10
print(f"If Unique characters quantity more than 10?: {len(characters_set) > 10}")
