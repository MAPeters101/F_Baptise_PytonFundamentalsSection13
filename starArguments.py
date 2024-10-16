def my_func(*args):
    print(type(args))
    print(args)

print(my_func())
print(my_func(1))
print(my_func(1, 2, 3, 4, [1, 2], 'abc'))

def my_func(a, b, *args):
    print(a)
    print(b)
    print(args)

print(my_func(1, 2))
print(my_func(1, 2, 3, 4, 5))

# def my_func(a, b, *args, c):
#     print(a)
#     print(b)
#     print(args)
#
# print(my_func(1, 2, 3, 4, 5))

def my_func(a, b, *args, c=5):
    print(a)
    print(b)
    print(args)
    print(c)

print(my_func(1, 2, 3, 4, 5))

# def my_func(a, b, *args, *extras):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#
# print(my_func(1, 2, 3, 4, 5))

print(sum({1,2,3}))

def average(*values):
    return sum(values) / len(values)

print(average(1))
print(average(1,2,3))
#print(average())
print(average(1,3,5,7,9))


def average(*values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0

print(average(1))
print(average(1,2,3))
print(average())
print(average(1,3,5,7,9))
