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

def add(a, b, c):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    return a + b + c

result = add(1, 2, 3)
print(result)

def add(a, b, c):
    print('initial namespace:', locals())
    sum_ = a + b + c
    print('after sum namespace:', locals())
    return a + b + c

result = add(1, 2, 3)
print(result)

result = add(10, 20, 30)
print(result)

print('='*30)

def find_max(a, b, c):
    max_ = a
    if b > max_:
        max_ = b
    if c > max_:
        max_ = c
    return max_

print(find_max(10, 20, 30))

from datetime import datetime

def log(message):
    curr_time = datetime.utcnow().isoformat()
    #curr_time = datetime.now(datetime.UTC)
    print(f'{curr_time} - [{message}]')

result = log('Log 1')
print(result, type(result))
result = log('Log 2')




