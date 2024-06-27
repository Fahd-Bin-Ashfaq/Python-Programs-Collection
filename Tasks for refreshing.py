# Area OF Reactangle

width=float(input("Enter widh of rectangle: "))
length=float(input("Enter length of rectangle: "))

Area_of_rectAngle=width*length
print("Area Of Rectangle :",Area_of_rectAngle)

#Check Even Or Odd

number=int(input("Enter Nummber: "))
if number%2==0:
    print(number," 5is Even")

else:
    print(number," is odd")

# Reverse String
# string = "hello"
reversed_string = string[::-1]
print(reversed_string)

#Factorial

num=int(input("Enter Number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of ",num," is", fact)    

#palindrome
string = "radar"
cleaned_string = string.replace(" ", "").lower()
is_palindrome = cleaned_string == cleaned_string[::-1]

if is_palindrome:
    print(string," is a palindrome.")
else:
    print(string," is not a palindrome.")

#Fibonacci Series

a, b = 0, 1

num = int(input("Enter Number: "))
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b

#Find the Largest Among Three Numbers:

num=input("Enetr Three Numbers With Space,").split()
a, b, c = map(int, num)
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c
print("The largest number is:", largest)

#Calculate Simple Interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period in years: "))
simple_interest = (principal * rate * time) / 100
print("Simple Interest:", simple_interest)

#Convert Celsius to Fahrenheit:

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#Check if it's a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")


