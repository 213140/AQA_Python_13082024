def sum_of_numbers_from_list(input_list):
    sum_list = []
    for element in input_list:
        try:
            new_list = element.split(',')
            sum_of_list = 0
            for number_in_list in new_list:
                sum_of_list += int(number_in_list)
            sum_list.append(sum_of_list)
        except ValueError:
            sum_list.append("Не можу це зробити")
    return sum_list

some_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]
print(sum_of_numbers_from_list(some_list))

