if_h_found = False
while(True):
    entered_string = input("Please enter string which include 'h' or 'H' letter:")
    entered_string = entered_string.upper()
    list_of_characters = entered_string[::1]
    if(list_of_characters.count('H') <= 0):
        print("There is not 'h' or 'H' letters! Please repeat!")
        continue
    else:
        print("Letter was found!")
        break