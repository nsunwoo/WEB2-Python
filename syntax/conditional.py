user_id = input('ID: ')
user_pwd = input('Password: ')

# if user_pwd == '111111':
#     print('Hello, master.')
# else:
#     print('Who are you?')

# 조건문 중첩 가능
# if user_id == 'sw':
#     if user_pwd == '111111':
#         print('Hello, master.')
#     else:
#         print('Who are you?')
# else:
#     print('Who are you?')

# 논리 연산자 사용
if user_id == 'sw' and user_pwd == '111111':
    print('Hello, master.')
elif user_id == 'bibi' and user_pwd == '222222':
    print('Hello, master.')
else:
    print('Who are you?')