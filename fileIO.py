# with open("demo.txt", "r") as f:
#     data = f.read()
#     print(data)
# # f.write("\nThis is to showcase escape sequence character\n")

# import os
# os.remove("demo.txt")

# with open("practice.txt", "w") as f:
#     f.write("Hi everyone\nWe are learning FILE I/O\nusing JAVA\nI like programming in JAVA\n")

# with open("practice.txt", "r") as f:
#     data = f.read()
#     new_data = data.replace("JAVA", "Python")
#     print(new_data)
    
    
# with open("practice.txt", "w") as f:
#     f.write(new_data)

# def check_for_word(word):
#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f:
#         data = f.readline()
#         while data:
#             data = f.readline()
#             if(word in data):
#                 print(line_no)
#                 return 
#             else:
#                 line_no += 1
#                 print(line_no)
                
#     return -1
    

# check_for_line()
# check_for_word("learning")

'''Code to find even numbers from practice.txt file'''        
count = 0
with open("practice.txt", "r") as f:
    data = f.read()
    # print(data)
    
    nums = data.split(",")
    # print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            print(val, end=" ")
            count += 1
            

print(f"\nThe number of even numbers: {count}")

