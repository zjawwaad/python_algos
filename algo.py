def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else: 
        return False


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True 
    else:
        if not a_smile and not b_smile:
            return True
    return False
    

def sum_double(a, b):
    if a==b:
        return (a+b)*2 
    else:
        return a+b

def sum_double(a, b):
# Store the sum in a local variable
    sum = a + b
    if a == b:
        sum = sum * 2
    return sum


def diff21(n):
    if n > 21:
        return (n-21)*2
    else: 
        return 21-n


def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False

def near_hundred(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return False

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)


def not_string(s):
    if s.startswith("not"):
        return s
    else:
        return "not " + s


def not_string(s):
    return s if s.startswith("not") else "not " + s


def missing_char(str, n):
    front = str[:n]
    back = str[n+1:]
    return front + back


def front_back(s):
    if len(s) >= 2:
        return s[-1] + s[1:-1] + s[0]
    else:
        return s

s = "hello"
# The last character: "o"
last_char = s[-1]

# The slice of characters from index 1 to -1 (excluding the first and last): "ell"
middle_chars = s[1:-1]

# The first character: "h"
first_char = s[0]

# Concatenating the parts together: "oellh"
result = last_char + middle_chars + first_char


def front_back(str):
    if len(str) >= 2:
        return str[-1] + str[1:-1] + str[0]
    else:
        return str



# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.


def front3(str):
    if str >= 3:
        return str[0:3]*3
    else:
        return str*3

def string_times(str, n):
    return str*n
