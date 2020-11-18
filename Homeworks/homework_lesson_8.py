# Task 1
def oops():
    raise IndexError


def function_that_calls_oops():
    try:
        oops()
    except IndexError:
        print('ошибка IndexError')
    except KeyError:
        print('ошибка KeyError')


function_that_calls_oops()

# Task 2


def function_that_takes_in_two_numbers(a=input('number 1?\n'), b=input('number 2?\n')):
    try:
        a = int(a)
        b = int(b)
        result = a * a / b
        return result
    except ZeroDivisionError:
        print('cannot divide by zero')
    except TypeError:
        print('wrong type')


function_that_takes_in_two_numbers()
