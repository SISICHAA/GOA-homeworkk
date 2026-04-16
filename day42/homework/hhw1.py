def remove_char(s):
    return s[1: -1]

def double_integer(i):
    return i * 2




def greet(name):
    return "Hello, " + name + " how are you doing today?"


def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2
    return None



def sum_array(a):
    total = 0
    for num in a:
        total += num
    return total



def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    