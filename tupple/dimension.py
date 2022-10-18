#Nested tuple
integers_one = (1, 8, 12, 13, 20)

integers_two = (2, 23, 12, 9, 8)

for i in integers_one:
    for j in integers_two:
        if i == j:
            print(i, j)
