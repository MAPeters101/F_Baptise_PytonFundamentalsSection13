
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
print()
print()


def parse(s, sep=',', strip=True):
    items = s.split(sep)
    if strip:
        return [item.strip() for item in items]
    else:
        return items

print(parse('  a , b,  c  '))
print(parse('  a , b,  c  ', strip=False))
print(parse('a:b : c: d'))
print(parse('a:b : c: d', sep=':'))
print(parse('a\n|b\n|c\n', sep='|'))
print(parse('a\n|b\n|c\n', sep='|', strip=False))
print()


print('a', 'b', 'c', sep='---')
print(*'abc', sep=',', end='***')
print('next print line')
print()

print(*'abc', sep=',', end='***\n')
print('next print line')
print()

print('='*80)

data = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

def process_data(data, item_sep=',', line_sep='\n'):
    output = ''

    for row in data:
        for element in row:
            output += str(element) + item_sep
        output += line_sep

    return output

print(process_data(data))
print(process_data(data, item_sep='==', line_sep='\n\n'))

print(process_data(data))
print('done')
print()


print('-'.join(['a', 'b', 'c']))
print(','.join(['a', 'b', 'c']))
print()


def process_data(data, item_sep=',', line_sep='\n'):
    output = ''
    for row in data:
        row_str = item_sep.join([str(el) for el in row])
        output += row_str + line_sep
    return output

print(process_data(data))
print('done')
print()

print(process_data(data, line_sep='=='))
print('done')
print()
print('-'*30)


def process_data(data, item_sep=',', line_sep='\n'):
    output = ''
    for row in data:
        row_str = item_sep.join(str(el) for el in row)
        output += row_str + line_sep
    return output

print(process_data(data))
print('done')
print()

print(process_data(data, line_sep='=='))
print('done')
print()
print('-'*30)




