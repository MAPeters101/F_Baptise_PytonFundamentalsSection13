
def func(a=1):
    return a

print(func())
print(func(10))
print(func(a=20))

def func(a, b=10, c=20):
    return a, b, c

print(func(1))
print(func(1, 2))
print(func(1, 2, 3))
print(func(1, c=100))
print()

def is_close(a, b, abs_tol=0.01):
    return abs(a - b) <= abs_tol

print(is_close(1.255, 1.256))
print(is_close(1255, 1256))
print(is_close(1255, 1256, abs_tol=5))



