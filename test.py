'''1'''

# vowel = []
# char = input("Enter a character: ")
# if char in "aeiouAEIOU":
#     print(f"The character {char} is a Vowel...")
#     vowel.append(char)
#     print(vowel)
# else:
#     print(f"The character {char} is a Consonant. Therefore the ASCII value is -> {ord(char)}")

'''2'''

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# if num1 > num2:
#     if num1 > num3:
#         print(f"{num1} is the greatest...")
#     else:
#         print(f"{num3} is the greatest...")
# else:
#     if num2 > num3:
#         print(f"{num2} is the greatest...")
#     else:
#         print(f"{num3} is the greatest...")

'''3'''

angle_a = int(input("Enter angle A: "))
angle_b = int(input("Enter angle B: "))
angle_c = int(input("Enter angle C: "))

if angle_a == angle_b:
    if angle_a == angle_c:
        print("The Triangle is an Equilateral Triangle...")
elif angle_a == angle_c:
    if angle_b >= 90:
        print("The Triangle is an Isosceles Triangle...")
else:
    print("The Triangle is an Scelene Triangle...")