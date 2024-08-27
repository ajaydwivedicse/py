# Write a function called calculate_area that takes base and height as an input and returns and
# area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height
# Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape
#
# Write a function called print_pattern that takes integer number as an argument and prints following pattern
# if input number is 3,
# *
# **
# ***
# if input is 4 then it should print
#
# *
# **
# ***
# ****
#  Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

# def calculate_area(base, height):
#     area = 1/2*base*height
#     return area

def calculate_area(dim1, dim2, shape_type='triangle'):
    '''

    :param dim1: dimension 1 of the given shape
    :param dim2: dimension 2 of the given shape
    :param shape_type: Either it will be traingle or rectangle. default is triangle
    :return: calculated area of the given shape
    '''
    if shape_type == 'triangle':
        area = 1 / 2 * dim1 * dim2
        return area
    elif shape_type == 'rectangle':
        area = dim1 * dim2
    else:
        print('Error: Input shape is neither triangle or rectangle')
        area = None
    return area


def print_pattern(num=5):
    '''
    This function will print the pattern accroding to given number
    :param num: input number
    :return: nothing
    '''
    for i in range(num):
        s = ''
        for j in range(i + 1):
            s += '*'
        print(s)


help(calculate_area)
print(calculate_area(4, 6, 'rectangle'))
print(print_pattern(5))
