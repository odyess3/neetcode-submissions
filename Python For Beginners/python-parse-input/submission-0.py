from typing import List

def read_integers() -> List[int]:
    user_input = input()
    lists = user_input.split(",")

    lists2 = []
    for i in lists:
        lists2.append(int(i))

    return lists2

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
