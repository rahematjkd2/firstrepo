list = [1,2,3,4,5,6,7]
veggies = ['potato','brinjal','ladyfinger','cucumber']
tuple = (1,2,3,4,5)

str = "macbook"
'''
for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("END")'''

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)

x = 49
idx = 0
# for el in nums:
#     if(el == x):
#         print("number found at index", idx)
#         break
#     idx += 1
    
# print(str[0])

# seq = range(10)

# print(seq[0])
# print(seq[1])
# print(seq[2])
# print(seq[3])
# print(seq[4])

# for i in range(10): #range(stop)
    # print(i)


# for i in range(2,10): #range(start,stop)
#     print(i)


# for i in range(2,10,2): #range(start,stop,step)
#     print(i)

# for i in range(1,100,2):
#     print(i)

# Print numbers from 1 to 100
# for i in range(100,0,-1):
#     print(i)
#Multiplication of a input number
# n = int(input("Enter number : "))

# for i in range(1,11):
#     print(n * i)

for i in range(5):
    pass    #empty loop

if i > 5:
    pass

# print("some useful work")

# n = int(input("Enter a number: "))
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1

# # for i in range(1, n+1):
# #     sum += i
    
# print("Total sum = ",sum)

n = int(input("Enter a number: "))
fact = 1
i = 1

# while i <= n:
#     fact *= i
#     i += 1

for i in range(i, n+1):
    fact *= i

print(f"Factorial of {n} = {fact}")