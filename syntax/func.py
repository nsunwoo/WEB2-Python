a = 1
b = 2
c = 3
s = a + b + c
r = s / 3
print(r)

# def average():
#     a = 1
#     b = 2
#     c = 3
#     s = a + b + c
#     r = s / 3
#     print(r)

# average()

# # Input
# def average(a, b, c):
# # a, b, c -> 'parameter(매개변수)'
#     s = a + b + c
#     r = s / 3
#     print(r)

# average(10, 20, 30)
# # 10, 20, 30 -> 'argument(인자)'

def average(a, b, c):
    s = a + b + c
    r = s / 3
    return r

print(average(10, 20, 30))