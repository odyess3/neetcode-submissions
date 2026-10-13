def nested(min: int, max: int):
    i, j = 0, 0

    for i in range(min, max):
        for j in range(min, max):
            print(i,j)


nested(3,6)