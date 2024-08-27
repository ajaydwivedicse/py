x = input('Enter number1: ')
y = input('Enter number1: ')

try:
    z = x / int(y)
except ZeroDivisionError as e:
    print('Division by zero')
    z = None

except Exception as e:
    print('Exception type: ', type(e).__name__)
    z = None
print('Division is: ', z)