book_count = 10
read_count = 0

print('Ibu said, "Read your book"')

understood_count = 0

print(f"Total already read {understood_count}")

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f"Book to-{understood_count + 1} NOT UNDERSTAND")
    else:
        understood_count = understood_count + 1
        print(f"Book to-{understood_count} UNDERSTAND")

print(f"Total already read {understood_count}")

if understood_count == book_count:
    print(f'all books have been read and understood')
else:
    print(f'"Not all books can be understood, I can only understand {understood_count} buku"')
