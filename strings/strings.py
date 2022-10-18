s = "2QaXySWWrt"
str_ = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']
for i in str_:
    result = []
    for j in s:
        result.append(eval(f'j.{i}()'))
    if True in result:
        print('True')
    else:
        print('False')
