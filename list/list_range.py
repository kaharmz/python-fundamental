
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

#merge two list
programming_languages = [
    'Python',
    'Javascript',
    'Typescript',
    'Java',
    'Kotlin',
    'Golang',
    'R',
    'Cobol',
    'C#',
    'C++',
    'Php'
]

#add new programming languages to list
programming_languages[4] = 'Dart'

used = ['99%', '80%', '70%', '60%', '50%', '40%', '30%', '20%', '10%', '55%', '65%']

#add new used precentage
used[4] = '64%'

popularity = [list(i) for i in zip(programming_languages, used)]

#3 popular in the world
for j in popularity[0:5]:
    print(j)


