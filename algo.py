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