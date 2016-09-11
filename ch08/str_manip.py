# Example of Python string manipulation

a = "hello"
b = 'world'
c = '''a multiple
line string'''
d = """More
multiple"""
c = ("Three " "strings " "Together")

s = "hello world"
print(s.count('l'))
try:
    print(s.rindex('m'))
except ValueError as e:
    print(e)

s = "hello world, how are you"
s2 = s.split(' ')
print(s2)
print('#'.join(s2))
print(s.replace(' ', '**'))
print(s.partition(' '))
