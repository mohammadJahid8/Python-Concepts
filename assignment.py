# Assignment by Mohammad Jahid

# experiment 1
# print('Do Not Adopt Unfairmeans in  the exam')

# experiment 2 
# print('Welcome to python programming') 


# experiment 3-Find the sum of two numbers
# Number1 = int(input('Enter the first number: '))
# Number2 = int(input('Enter the second number: 
# ))
# sum = Number1 + Number2
# print('Summation is: ' , sum)

# experiment 4- find the summation of two float numbers
# Number1 = float(input('Enter the first number: '))
# Number2 = float(input('Enter the second number: '))
# sum = Number1 + Number2
# print('Summation is: ' , sum)







# experiment 5 take string as input 
# String = input('Enter the string: ')
# print('String is: ' , String)


# experiment 6
# Number1 = (input('Enter the first number: '))
# Number2 = (input('Enter the second number: '))
# result = Number1 + Number2
# print('Result is: ' , result)


# experiment 7
# String1 = input('Enter the first String: ')
# String2 = input('Enter the second String: ')
# result = String1 + String2
# print('Result is: ' , result)





# experiment 8
# Number1 = (input('Enter the first number: '))
# Number2 = (input('Enter the second number: '))
# remainder = int(Number1) % int(Number2)
# print('remainder is: ' , remainder)


# experiment 9
# Number1 = (input('Enter the first number: '))
# Number2 = (input('Enter the second number: '))
# division = float(Number1) / float(Number2)
# print('division is: ' , division)



# Experiment 2

# problem 1
# n = int(input('Enter the number: '))
# if n < 0:
#     print('Enter a positive number')
# else:
#     sum = 0

#     while(n > 0):
#         sum += n
#         n -= 1
#     print('Sum is: ', sum)


# problem 2- find the average of some numbers
# numbers = [0, 1, 2, 3]
# numbers[0] = int(input('Enter the first number: '))
# numbers[1] = int(input('Enter the second number: '))
# numbers[2] = int(input('Enter the third number: '))
# numbers[3] = int(input('Enter the fourth number: '))

# average = (numbers[0] + numbers[1] + numbers[2] + numbers[3]) / 4
# print('Average is: ', average)


# problem 3- convert celsius to fahrenheit
# celsius = float(input('Enter the celsius: '))
# fahrenheit = (celsius * 9/5) + 32
# print('Fahrenheit is: ', fahrenheit)


# problem 4- convert fahrenheit to celsius
# fahrenheit = float(input('Enter the fahrenheit: '))
# celsius = (fahrenheit - 32)/1.8
# print('%0.1f degree fahrenheit is = %0.1f degree celsius' %(fahrenheit, celsius))

# problem 5 - Convert Kilometers to Miles
# kilometers = float(input('Enter the kilometers: '))
# conv_factor = 0.621371
# miles = kilometers * conv_factor
# print('%0.3f kilometers is = %0.3f miles' %(kilometers, miles))

# prblem-6 Find the area of rectangle
# Length = int(input('Enter the length: '))
# Width = int(input('Enter the width: '))
# Area = Length * Width
# print('Area is: ', Area)


# problem-7 Find the area of circle
# import math
# radius = float(input('Enter the radius: '))
# Area = math.pi * radius * radius
# print('Area is: ', Area)


# problem 8- Find the area of sqaure
# Arm = float(input('Enter the Arm: '))
# Area = Arm * Arm
# print('Area is: ', Area)

# problem 9 - Find the area of rhombus
# Diagonal1 = float(input('Enter the Diagonal1: '))
# Diagonal2 = float(input('Enter the Diagonal2: '))
# Area = (Diagonal1 * Diagonal2) / 2
# print('Area is: ', Area)

# problem 10 - Find the Area and Volume of a Sphere
import math
radius = float(input('Enter the radius: '))
Area = 4 * math.pi * radius * radius
Volume = (4/3) * math.pi * radius * radius * radius
print('Area is: ', Area)
print('Volume is: ', Volume)