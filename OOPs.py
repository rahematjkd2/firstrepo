# # class Student:
# #     #default constructors
# #     def __init__(self): 
# #         pass
# #     college_name = "ABC College"
# #     name = "anonymous" #class attrib
# #     #Parameterized constructors
# #     def __init__(self, name, marks): #Constructor initialization
# #         self.name = name #obj attrib >(more precedence) class attrib
# #         self.marks = marks
# #         print("adding new student in database..")


# # class Student:
# #     college_name = "ABC College"
    
# #     def __init__(self, name, marks): #Constructor initialization
# #         self.name = name #obj attrib >(more precedence) class attrib
# #         self.marks = marks
        
# #     def welcome(self):
# #         print("Welcome student,", self.name)
    
# #     def get_marks(self):
# #         return self.marks
        
        
# # s1 = Student("Rahemat", 97)
# # s1.welcome()
# # print(s1.name, s1.get_marks())
# '''Practice Question'''
# '''1'''
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod   #decorator
#     def college():
#         print("ABC College")
    
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(f"Hi {self.name} your average score is: {sum / 3}")
        
# # s1 = Student("Tony Stark", [99, 97, 98])
# # s1.get_avg()
# # s1.college()
# # s1.name = "Iron Man"
# # s1.get_avg()

# '''2'''
# '''Banking System'''
# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
    
#     #debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print(f"Rs.{amount} was debited from your account {self.account_no}.")
#         print(f"Total balance: {self.get_balance()}")
    
#     #credit method
#     def credit(self, amount):
#         self.balance += amount
#         print(f"Rs.{amount} was credited in your account {self.account_no}.")
#         print(f"Total balance: {self.get_balance()}")
        
#     def get_balance(self):
#         return self.balance
        
# acc1 = Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(200)
# acc1.credit(40000)
# acc1.debit(10000)
def getMaximumAmount(n, m, quantity):
    # Sort the quantities in descending order
    quantity.sort(reverse=True)
    
    max_revenue = 0
    for i in range(n):
        # The number of customers that can buy the current item
        if m <= 0:
            break
        sell = min(quantity[i], m)
        max_revenue += sell * (n - i)
        m -= sell
    
    return max_revenue

# Example usage
n = 5
quantity = [10, 10, 8, 9, 1]
m = 6
print(getMaximumAmount(n, m, quantity))  # Output: 55

