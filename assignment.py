# Assignment by Mohammad Jahid

# experiment 1
print('Do Not Adopt Unfairmeans in  the exam')

# experiment 2 
print('Welcome to python programming') 


# experiment 3-Find the sum of two numbers
Number1 = int(input('Enter the first number: '))
Number2 = int(input('Enter the second number: '))
sum = Number1 + Number2
print('Summation is: ' , sum)

# experiment 4- find the summation of two float numbers
Number1 = float(input('Enter the first number: '))
Number2 = float(input('Enter the second number: '))
sum = Number1 + Number2
print('Summation is: ' , sum)


# experiment 5 take string as input 
String = input('Enter the string: ')
print('String is: ' , String)


# experiment 6
Number1 = (input('Enter the first number: '))
Number2 = (input('Enter the second number: '))
result = Number1 + Number2
print('Result is: ' , result)


# experiment 7
String1 = input('Enter the first String: ')
String2 = input('Enter the second String: ')
result = String1 + String2
print('Result is: ' , result)





# experiment 8
Number1 = (input('Enter the first number: '))
Number2 = (input('Enter the second number: '))
remainder = int(Number1) % int(Number2)
print('remainder is: ' , remainder)


# experiment 9
Number1 = (input('Enter the first number: '))
Number2 = (input('Enter the second number: '))
division = float(Number1) / float(Number2)
print('division is: ' , division)



# Experiment 2

# problem 1
n = int(input('Enter the number: '))
if n < 0:
    print('Enter a positive number')
else:
    sum = 0

    while(n > 0):
        sum += n
        n -= 1
    print('Sum is: ', sum)


# problem 2- find the average of some numbers
numbers = [0, 1, 2, 3]
numbers[0] = int(input('Enter the first number: '))
numbers[1] = int(input('Enter the second number: '))
numbers[2] = int(input('Enter the third number: '))
numbers[3] = int(input('Enter the fourth number: '))

average = (numbers[0] + numbers[1] + numbers[2] + numbers[3]) / 4
print('Average is: ', average)


# problem 3- convert celsius to fahrenheit
celsius = float(input('Enter the celsius: '))
fahrenheit = (celsius * 9/5) + 32
print('Fahrenheit is: ', fahrenheit)


# problem 4- convert fahrenheit to celsius
fahrenheit = float(input('Enter the fahrenheit: '))
celsius = (fahrenheit - 32)/1.8
print('%0.1f degree fahrenheit is = %0.1f degree celsius' %(fahrenheit, celsius))

# problem 5 - Convert Kilometers to Miles
kilometers = float(input('Enter the kilometers: '))
conv_factor = 0.621371
miles = kilometers * conv_factor
print('%0.3f kilometers is = %0.3f miles' %(kilometers, miles))

# prblem-6 Find the area of rectangle
Length = int(input('Enter the length: '))
Width = int(input('Enter the width: '))
Area = Length * Width
print('Area is: ', Area)


# problem-7 Find the area of circle
import math
radius = float(input('Enter the radius: '))
Area = math.pi * radius * radius
print('Area is: ', Area)


# problem 8- Find the area of sqaure
Arm = float(input('Enter the Arm: '))
Area = Arm * Arm
print('Area is: ', Area)

# problem 9 - Find the area of rhombus
Diagonal1 = float(input('Enter the Diagonal1: '))
Diagonal2 = float(input('Enter the Diagonal2: '))
Area = (Diagonal1 * Diagonal2) / 2
print('Area is: ', Area)

# problem 10 - Find the Area and Volume of a Sphere
import math
radius = float(input('Enter the radius: '))
Area = 4 * math.pi * radius * radius
Volume = (4/3) * math.pi * radius * radius * radius
print('Area is: ', Area)
print('Volume is: ', Volume)

# Experiment 3

# Problem 1- Conversion of days to month and days
Days = int(input('Enter the days: '))
Month = Days // 30
Day = Days % 30 
print("Converstion of {0} Days to Month and Days is {1} Month and {2} Days".format(Days, Month, Day))


# Problem 2- Find the area of a triangle
Base = float(input('Enter the Base: '))
Height = float(input('Enter the Height: '))
Area = (Base * Height) / 2
print('Area is: ', Area)

# Problem 3- Find the smallest number between two numbers
Number1 = int(input('Enter the first number: '))
Number2 = int(input('Enter the second number: '))
if Number1 < Number2:
    print('Smallest number is: ', Number1)
else:
    print('Smallest number is: ', Number2)


# Problem 4- Uses of different input-output operators
x = 10
y = 20
z = 30
m = 5*x^3
n = (x+y) + (y*z) -4*x*y
p = (x*y) >= (5+x)-2
q = (x+y) <= (x*y)
L = (x>y) and (x<y)
x *= 3
print(x)
print(m)
print(n)
print(p)
print(q)
print(L)

# Problem 5- find even or odd
Number = int(input('Enter the number: '))
if Number % 2 == 0:
    print('Even')
else:
    print('Odd')

# Problem 6- Swap two numbers
x = input('Enter the number: ')
y = input('Enter the number: ')
temp = x
x = y
y = temp
print('After swapping: ', x, y)

# # Problem 1- find if the number is negetive, positive or zero
Number = float(input('Enter the number: '))
if Number >= 0:
    if Number == 0:
        print('Zero')
    else:
        print('Positive')
else:
    print('Negative')


# Problem 2-Find the largest number between three numbers
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
num3 = int(input('Enter the third number: '))
if num1 > num2 and num1 > num3:
    print('Largest number is: ', num1)
elif num2 > num1 and num2 > num3:
    print('Largest number is: ', num2)
else:
    print('Largest number is: ', num3)



# Problem 3-Find the leap year 
Year = int(input('Enter the year: '))
if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0:
    print('Leap year')
else:
    print('Not a leap year')
         

# Problem 4- Find the prime number
Number = int(input('Enter the number: '))
if Number > 1:
    for i in range(2, Number):
        if (Number % i) == 0:
            print('Not a prime number')
            break
    else:
        print('Prime number')
else:
    print('Not a prime number')

# Problem 5- Find the factorial of a number
Number = int(input('Enter the number: '))
factorial = 1
if Number < 0:
    print('Factorial does not exist')
elif Number == 0:
    print('Factorial is 1')
else:
    for i in range(1, Number + 1):
        factorial = factorial * i
    print('Factorial is: ', factorial)


# Experiment 5
# Problem 1- Display the even number in 1-10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

# Problem 2- Display the prime number in 1-10
lower = int(input('Enter the lower limit: '))
upper = int(input('Enter the upper limit: '))
print('Prime numbers between', lower, 'and', upper, 'are:')
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Problem 3- Find the summation of any digit
Sum = 0
Number = int(input('Enter the number: '))
while Number > 0:
    Reminder = Number % 10
    Sum = Sum + Reminder
    Number = Number // 10
print('Sum of the digits is: ', Sum)

# # Problem 4- Display the multiplication table of any number
Number = int(input('Enter the number: '))
for i in range(1, 11):
    print(Number, 'x', i, '=', Number * i)


# Problem 5- Display the pattern
for i in range(0,5):
    for j in range(0,i+1):
        print('*', end='')
    print()

# Problem 6- Display the pattern
k = 1
for i in range(0,5):
    for j in range(0,i+1):
        print(k, end='')
        k += 1
    print()
