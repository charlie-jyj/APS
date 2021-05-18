line = '안녕하세요'

# immutable
# String 의 내장함수는 return 값이 있다.

# replace
print(line.replace('세','시'))
print(line)
line = line.replace('세','시')
print(line)

# split
print(line.split('하'))

# isalpha
password = 'ab1c2d'
flag_alpha = False
flag_number = False
for char in password:
    if char.isalpha():
        flag_alpha = True

    if char.isdigit():
        flag_number = True

if not flag_alpha:
    print('알파벳이 사용되지 않았다.')
elif not flag_number:
    print('숫자가 사용되지 않았다.')
else:
    print('완벽한 비밀번호이다.')


# find
line2 = '안녕하세요'
print(line2.find('안'))
print(line2.index('ㅎ'))