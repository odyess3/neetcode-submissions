def divide_numbers(a: str, b: str) -> None:
    

    try:
        a,b = int(a), int(b)
        answer = a/b
        print(answer)

    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception in i:
        print("Error:" , i)
    



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
