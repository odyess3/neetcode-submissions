def add_two_numbers() -> int:
    user_input = input()

    lists = user_input.split(",")

    lists2 = []

    for i in lists:
        lists2.append(int(i))
    
    return sum(lists2)        



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
