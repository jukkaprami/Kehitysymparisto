# 1
'''while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")'''

# 2
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    except TypeError:
        print('please check that arguments are numbers!')     
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(3, 0)
divide(4, 2)