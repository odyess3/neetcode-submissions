your_dict = { 
  "a": 10, 
  "apple": 12,
  "bat": 7
}

def print_dict(my_dict: dict[str]):
  return my_dict

def print_dict_a(my_dict: dict[str],  value: str):
  return my_dict[value]

def print_dict_if_d(my_dict: dict[str],  value: str):
    if value in my_dict:
      return True
    else:
      return False
  

def print_dict_ressign(my_dict: dict[str],  value: str, replace: int):
    my_dict[value] = replace
    return my_dict
  


print(print_dict(your_dict))
print(print_dict_a(your_dict, "a"))
print(print_dict_if_d(your_dict, "d"))
print_dict_ressign(your_dict, "a", 4)
print(print_dict(your_dict))


