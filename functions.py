# # Function definition
# def calc_sum(a, b): #parameters
#     return a + b

# sum = calc_sum(178, 2221) #function call; arguments
# print(sum)

# def print_hello():
#     print("Hello")

# output = print_hello()
# print(output) #None

#Average of 3 numbers

# def calc_avg(num1, num2, num3):
#     sum = num1 + num2 + num3
#     avg = sum / 3
#     print(avg)
#     return avg

# calc_avg(98, 97, 95)

# def calc_prod(a=1, b=1):
#     return a * b

# print(calc_prod(24, 2))

cities = ["delhi", "bangalore", "hyderabad", "pune", "chennai", "mumbai"]

def print_len(list):
    print(len(list))
    
# print_len(cities)
    
def print_lists(list):
    for items in list:
        print(items, end=" ")

def calc_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact) 

# calc_fact(5)

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

# converter(73)

####################################################################
"""RECURSION"""

def fact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n - 1)
        

# print(fact(5))

def cal_sum(n):
    if(n == 0):
        return 0
    # print(n)
    return n + cal_sum(n - 1)

# print(cal_sum(100))

def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx], end=" ")
    print_list(list, idx + 1)
    print()
    
# print_list(cities, 2)

        


