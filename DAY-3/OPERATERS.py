integer_age = int(input("Enter your age: "))
float_hight = float(input("Enter your hight value: "))
iota = 5 + 5j
height = float(input("the hight of triangle:"))
base = float(input("enter the base of triangle:"))
area_of_triangle = 0.5 * base * height
print(f"the area of the triangle is {area_of_triangle}")
side1 = input("enter the side 1 of triangle:")
side2 = input("enter the side 2 of triangle:")
side3 = input("enter the side 3 of triangle:")
perimeter_of_triangle = (side1 + side2 + side3)
print(f"the perimenter of triangle is : {perimeter_of_triangle}")
length_of_rectangle = float(input("enter the length of rectangle:"))
breadth_of_rectangle = float(input("enter the breadth of rectangle:"))
area_of_rectangle = breadth_of_rectangle * length_of_rectangle
perimeter_of_rectangle = (breadth_of_rectangle + length_of_rectangle)
print(f"the area of the rectangle is : {area_of_rectangle}")
print(f"the perimenter of the rectangle is : {perimeter_of_rectangle}")
radiusOfCircle = float(input("enter the radius of circle:"))
areaOfCircle = radiusOfCircle * radiusOfCircle * 3.147
perimeterOfCircle = 2 * 3.147 * radiusOfCircle
print(f"the area of the circle is : {areaOfCircle}")
print(f"the perimenter of the circle is : {perimeterOfCircle}")

def analyze_line(m, b):
  # Slope is directly given by m
  slope = m

  # y-intercept occurs when x = 0 -> (0, b)
  y_intercept = (0, b)

  # x-intercept occurs when y = 0 -> 0 = mx + b -> x = -b / m
  if m != 0:
    x_intercept = (-b / m, 0)
  else:
    x_intercept = "None (horizontal line)"

  return slope, x_intercept, y_intercept


Equation: y = 2x - 2
m = 2
b = -2

slope, x_int, y_int = analyze_line(m, b)

print(f"Slope: {slope}")
print(f"x-intercept: {x_int}")
print(f"y-intercept: {y_int}")

import math
pointOne = (2,2)
pointTwo = (6,10)
slope_M = (pointTwo[1]-pointOne[1]) / (pointTwo[0]-pointOne[0])
horizontal_distance = pointTwo[0]-pointOne[0]
distance = horizontal_distance * math.sqrt(1 + slope_M * slope_M)

print(f"slope is : {slope_M}")
print(f"horizontal distance is : {distance}")

word1= len("python")
word2= len("Dragon")
compare = bool(word1 != word2)
print(compare)

word1 = 'python'
word2 = 'dragon'

print(f"on is present in python {bool(word1.find('on') != -1)}")
print(f"on is present in dragon {bool(word2.find('on') != -1)}")

if word1.find('on') != -1 and word2.find('on') != -1:
    print("on is present in python and dragon")

sentence = 'I hope this course is not full of jargon.'
sentence.find('jargon')
if sentence.find('jargon') != -1:
  print('present')
else:
  print('not present')

word = len("pyhton")
print(word)
print(float(word))
print(str(word))

number = int(input('type your number: '))
check = number % 2
if check == 0:
  print(number, 'is even')
else:
  print(number, 'is odd')
