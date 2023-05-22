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

