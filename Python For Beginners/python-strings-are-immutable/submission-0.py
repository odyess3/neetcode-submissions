def remove_fourth_character(word: str) -> str:
    before_4 = word[:3]
    after_4 = word[4:]
    new = before_4+after_4
    return new


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
