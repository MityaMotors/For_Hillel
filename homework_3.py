import requests  # pip3 install requests   / pip install requests
import string
# integer, Float
i = 100
f = 100.5

string.digits
string.punctuation

# String objects
var = ""  # 'abc', '''abc''', """abc"""
v = str()
s60 = '*' * 60
si = str(i)
si1 = si.replace('1', '0')
si.lower()
"".isdigit()

"""
This module created for:
    - test purpose
    - ...
"""

# Tuple
t = tuple()
var_tuple = 1, 2, 3, "abc", "", True, False, None, (0, 0), (10, 25)
var_tuple = (1, 2, 3, "abc", "", True, False, None, (0, 0), (10, 25))
# var_tuple = (1, 2, 3)
# var_tuple = var_tuple[:-1]
t1 = (None,) * 50
t2 = tuple(str(f))
t21 = f,
t3 = (i, f)
t1.count(None)
t1.index(None)
var_tuple = var_tuple[:4] + (var_tuple[-1],)
# var_tuple[3] = 10


# List
l = list()
l1 = [1, 2, 3, "abc", "", True, False, None, (0, 0), (10, 25), [], [0, 4]]
l2 = [None] * 40
l3 = list((i, f))   # l2 = list(t3)
l1.count(10)


respond = requests.get('https://rozetka.com.ua/214936693/p214936693/')
data = respond.text
"""
>>> x = si
>>> x
'100'
>>> si = '101'
>>> x
'100'
>>> x = si[0]
>>> x
'1'
>>> si = '123456789'
>>> x = si[0:6]
>>> x
'123456'
>>> x = si[0:5]
>>> x
'12345'
>>> si = '0123456789'
>>> x = si[0:5]
>>> x
'01234'
>>> x = si[0:6]
>>> x
'012345'
>>> x2 = si[:]
>>> x2
'0123456789'
>>> x3 = si[-1]
>>> x3
'9'
>>> x4 = si[-3:-1]
>>> x4
'78'
>>> x5 = si[-2:]
>>> x5
'89'
>>> x2 = si[  : ]
>>> x
'012345'
>>> si
'0123456789'
>>> x2
'0123456789'
>>> x5 = si[::-1]
>>> x5
'9876543210'
>>> x5 = si[ : : 2]
>>> x5
'02468'
>>> x5 = si[ : : 3]
>>> x5
'0369'
>>> x5 = si[ : : 5]
>>> x5
'05'
>>> x5 = si[ : : 6]
>>> x5
'06'
>>> x5 = si[ : : 12]
>>> x5
'0'
>>> x6 = si[5:12]
>>> x6
'56789'
>>> x1 = si[12]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
"""
# Get price and comments count



x = ''

if "abc" in "asjklvbadjvbjvjkbvbjabc":
    print('yes')
    x = x + 'abc'

if "c" in "asjklvbadjvbjvjkbvbjabc":
    print('yes')
    x = x + 'c'