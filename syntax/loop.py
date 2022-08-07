# list
print(1)
for value in ['a', 'b', 'c']:
    print(value)
print(2)

print('---')

# range
for value in range(10):
    print(value)
    value = 5 # this will not affect the for-loop
              # because value will be overwritten
              # with the next index in the range