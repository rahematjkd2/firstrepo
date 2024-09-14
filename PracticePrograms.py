"""*************** Input and output statements ***************"""

'''1.Write a program to print the square of a given integer number'''

# num = int(input("Enter an integer number: "))
# square = num * num
# print(f"Sqaure of {num} is -> {square}")


'''2. Write a program to find the product of two float numbers.'''

# num1 = float(input("Enter 1st float number: "))
# num2 = float(input("Enter 2nd float number: "))
# print(f"The product of {num1} and {num2} is -> {num1 * num2}")

'''3. Write a program to find the area of a rectangle.'''

# length = eval(input("Enter length of the rectangle: "))
# breadth = eval(input("Enter breadth of the rectangle: "))
# area = length * breadth
# print(f"The Area of given rectangle is -> {area}")

'''4. Write a program to reverse the given string.'''

# str = input("Enter a String: ")
# reverse_str = str[::-1]
# print(f"The reverse of {str} is -> {reverse_str}")

'''5. Write a Program to find the sum, difference, product and division.Between 2 integer numbers.'''

# num1 = int(input("Enter 1st integer: "))
# num2 = int(input("Enter 2nd integer: "))
# print(f'''Sum of {num1} and {num2} is -> {num1 + num2}
# Difference of {num1} and {num2} is -> {num1 - num2}
# Product of {num1} and {num2} is -> {num1 * num2}
# Division of {num1} and {num2} is -> {num1 / num2}''')

'''6. Write a program to find the simple interest.'''

# principal = int(input("Enter principal amount: "))
# time = int(input("Enter time: "))
# roi = eval(input("Enter rate of interest: "))

# simple_interest = (principal * time * roi) / 100

# print(f'''
# Principal Amount : Rs.{principal}
# Time Period : {time} years
# Rate of Interest : {roi}%

# The Simple Interest is -> Rs.{simple_interest}
# ''')

'''7. Write a program to calculate area of triangle'''

# base = eval(input("Enter base of a triangle: "))
# height = eval(input("Enter height of a triangle: "))

# area_of_triangle = 0.5 * base * height

# print(f"The area of given Triangle is -> {area_of_triangle}")

'''8. Write a Python code to swap two variables.'''


'''9. Write a Python program to calculate the square root of a given number'''

# import math
# num = int(input("Enter an integer number: "))
# square_root = math.sqrt(num)
# print(f"The square root of {num} is -> {square_root}")


'''10. Write a Python program to find the area of a circle.'''

# PI = 3.14159265359

# radius = float(input("Enter the radius of a circle: "))
# area_of_circle = PI * (radius ** 2)
# print(f"The Area of a given circle is -> {area_of_circle}")

"""*************** Simple If ***************"""

'''11. Write a program To register.For a company only if job location is Bangalore.'''

# location = input("Enter the location: ")
# if location == 'Bangalore':
#     print("You are eligible to register for this Job")


'''12. Write a program to check whether the given number is even '''

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"The number {num} is an Even Number...")

'''13. Write a program to check whether the given number is odd '''

# num = int(input("Enter a number: "))
# if num % 2 != 0:
#     print(f"The number {num} is an ODD Number...")

'''14. Write a program to check whether the given number lies between 5 to 10'''

# number = int(input("Enter a number: "))
# if number in range(5,11):
#     print(f"The number {number} lies between 5 to 10...")

'''15. Write a program To check whether the given string is having more than three characters '''

# str = input("Enter a String: ")
# if len(str) > 3:
#     print(f"The String {str} contains more than 3 characters i.e. -> {len(str)} characters")

'''16. Write a program To check whether the given number is having 4 digits '''

# num = int(input("Enter a number: "))
# if len(str(num)) == 4:
#     print(f"The number {num} contains exactly {len(str(num))} digits...")

'''17. Write a program to check whether the given character is a vowel '''

# character = input("Enter a character: ")
# if character in ("aeiouAEIOU"):
#     print(f"The character {character} is a vowel...")

'''18. Write a program to check whether the given integer number is even and multiple of five'''

# number = int(input("Enter an integer number: "))
# if number % 2 == 0 and number % 5 == 0:
#     print(f"The number {number} is an Even number and Multiple of 5...")

'''19. Write a program.To check whether the given string is character '''

# str = input("Enter a string: ")
# if len(str) == 1:
#     print(f"The string {str} is a character...")

'''20. Write a program.To check whether the given character is uppercase alphabet '''

# char = input("Enter a single character: ")
# if char.isupper():
#     print(f"The character {char} is an UpperCase Alphabet...")

'''21. Write a program.To check whether the given character is lowercase alphabet '''

# char = input("Enter a single character: ")
# if char.islower():
#     print(f"The character {char} is an LowerCase Alphabet...")

'''22. Write a program to check whether the given character is digit '''

# character = input("Enter a character: ")
# if character.isdigit():
#     print(f"The character {character} is a Digit...")

'''23. Write a program to check whether the given character is alphabet '''

# character = input("Enter a character: ")
# if character.isalpha():
#     print(f"The character {character} is a Alphabet...")

'''24. Write a program to check whether the given character is a special character '''

# char = input("Enter a character: ")
# if char in ("`~!@#$%^&*()-_=+<,>./?:;{}[]"):
#     print(f"The character {char} is a Special Character...")

'''25. Write a program to check whether the given collection is List '''

# collection = eval(input("Enter a collection: "))
# if type(collection) is list :
#     print(f"The collection {collection} is a List Data Type...")

'''26. Write a program to check whether the entered value is default '''

# val = eval(input("Enter a value: "))
# if bool(val) == False:
#     print(f"The value entered {val} is a Default Value...")

'''27. Write a program to check whether The list consists of even number of values '''

# user_list = list(input("Enter an integer list: "))
# if (len(user_list) % 2) == 0:
#     print(f"The list {user_list} contains even number of elements...")
#     print(len(user_list))
# else:
#     print(len(user_list))

'''28. Write a program to check whether a list consists of middle value '''


'''29. Write a program to check whether the entered input is.Immutable. '''

# user_input = eval(input("Enter input: "))
# if type(user_input) in (str, tuple):
#     print(f"The input {user_input} is an Immutable DataType...")
    
'''30. Write a program to check whether the entered input is mutable.'''

# user_input = eval(input("Enter input: "))
# if type(user_input) not in (str, tuple):
#     print(f"The input {user_input} is a Mutable DataType...")  
    
'''31. Write a program to check whether The entered input is a single value '''

# user_input = eval(input("Enter input: "))
# if type(user_input) in (int, float, complex, bool):
#     print(f"The input < {user_input} > is a Single Value DataType...")

'''32. Write a program to check whether the entered input is multivalue or not.'''

# user_input = eval(input("Enter input: "))
# if type(user_input) not in (int, float, complex, bool):
#     print(f"The input < {user_input} > is a Multi Value DataType...")

'''33. Write a program to check whether the entered number is having only single Digit.'''

# num = int(input("Enter a number: "))
# if len(str(num)) == 1:
#     print(f"The number {num} entered is a Single Digit Number...")

'''34. Uni whether the first value present inside the given list is complex or not.'''

# user_list = eval(input("Enter a collection: "))
# if type(user_list[0]) is complex:
#     print(f"The first element {user_list[0]} is a Complex...")

'''35. Write a program to take and consider a tuple collection consisting of only two values. Check whether the taken tuple is homogeneous or heterogeneous.'''

# user_tple = eval(input("Enter a Tuple with only 2 values: "))
# if type(user_tple[0]) == type(user_tple[1]):
#     print(f"The tuple < {user_tple} > is a Homogenous Tuple...")

'''36. Write a program to check whether the given integer number is multiple of 10 or not.'''

# num = int(input("Enter an integer: "))
# if num % 10 == 0:
#     print(f"The entered number < {num} > is a Multiple of 10...")

'''37. Write a program to consider an integer number. If the number is even then print square of the number else print the cube of the number.'''

# num = int(input("Enter an Integer: "))
# if num % 2 == 0:
#     print(f"The Number {num} is an Even number. So Square of {num} is -> {num ** 2}...")
# else:
#     print(f"The Number {num} is NOT an Even number. So Cube of {num} is -> {num ** 3}...")

'''38. Write a program to check whether the given string is palindrome or not.'''

# input_str = input("Enter a string: ")
# reversed_str = input_str[::-1]
# if input_str == reversed_str:
#     print(f"The String {input_str} is a Palindrome -> {reversed_str}")

'''39. Write a program to consider string input, if it is having more than three characters then print length of the string else print string as it is.'''

# input_str = input("Enter a string: ")
# if len(input_str) > 3:
#     print(f"The string is a {len(input_str)} character String...")
# else:
#     print(f"The string does not contain more than 3 characters. So -> {input_str}")

'''40. Write a program to check whether the user is eligible to vote or not.'''

# age = int(input("Enter your Age: "))
# if age >= 18:
#     print("You are Eligible to vote...")

'''41. Write a program to check whether a number is divisible by 7 or not.'''

# num = int(input("Enter an integer: "))
# if num % 7 == 0:
#     print(f"The entered number < {num} > is Divisible by 7...")

'''42. Write a program to check whether the last digit of a number entered by the user is divisible by three or not.'''

# num = input("Enter a number: ")
# if int(num[-1]) % 3 == 0:
#     print(f"The last digit {num[-1]} of number {num} is Divisible By 3...")

'''43. Write a program to check whether the year is leap year or not.'''

# year = int(input("Enter a year: "))
# if year % 4 == 0:
#     print(f"{year} is a Leap Year...")

'''44. Write a program to check whether a number entered is a 3 digit number or not.'''

# num = input("Enter a number: ")
# if len(num) == 3:
#     print(f"{num} has 3 digits...")

'''45. Write a program to find the largest number out of two numbers expected from the user.'''

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# if num1 > num2:
#     print(f"Number 1 - {num1} is Largest...")
# else:
#     print(f"Number 2 - {num2} is Largest...")

'''46. Write a program to check whether a number.Entered by the user is positive or negative.'''

# num = int(input("Enter a Number: "))
# if num > 0:
#     print(f"{num} is a Positive Number")
# else:
#     print(f"{num} is a Negative Number")

'''47. Write a program.To check whether a number accepted from the user is divisible by two and three both.'''

# num = int(input("Enter a Number: "))
# if num % 2 == 0 and num % 3 == 0:
#     print(f"The number < {num} > is divisible by 2 and 3...")

"""*************** Elif Statement ***************"""

'''48.Write a program to check the relation between two integer numbers'''

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num2 < num1:
#     print(f"{num2} is less than {num1}")
# elif num1 == num2:
#     print(f"{num1} is Exactly equals to {num2}")

'''49. Write a program to check whether a given character is uppercase or lowercase or number. If character is uppercase print uppercase, If character is lowercase print lowercase. If the character is a number, print the ascii number of it. '''

# char = input("Enter a Character: ")
# if char.isupper():
#     print("Character is an Uppercase character...")
# if char.islower():
#     print("Character is an Lowercase character...")
# if char.isdigit():
#     print(f"The ASCII value of {char} is -> {ord(char)}")

50. 