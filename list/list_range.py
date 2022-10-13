
squares = []
for i in range(1, 52):
    #inserts the number from the loop to a list with a power of 2
    squares.append(i ** 2)

#slicing list with looping
for square in squares[1:25]:
    print(square)

#copy list
other_squares = squares[1:10]
for j in other_squares:
    print(j)


