def say_hello():
    return 'hello'

print(globals())
a = 100
print(globals())

result = say_hello()
print(result)

f = say_hello
print(f())

l1 = [1, 2, 3]
l2 = l1
print(l1 is l2)
print(globals())
print(f is say_hello)

print(say_hello())
print(f())

print(say_hello.__name__)
print(f.__name__)







