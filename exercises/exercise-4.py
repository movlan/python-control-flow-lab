# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter the lengths of three side of a triangle:')
a = float(input('a: '))
b = float(input('b: '))
c = float(input('c: '))
triangle_type = ''
if a == b == c:
    triangle_type = 'equilateral'
elif a == b or b == c or c == a:
    triangle_type = 'isosceles'
else:
    triangle_type = 'scalene'

print(f'A triangle with sides of {int(a)}, {int(b)} & {int(c)} is a {triangle_type} triangle')