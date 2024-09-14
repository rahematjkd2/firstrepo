# '<' Operator
print(10<22)
print((10,20)<(20,10))
print([1,2]<[1.0,2.0])
print('python'<'python')
print({10,20}<{20,10,30})

# '>' Operator
print(100>25)
print((1,2,3)>(3,2,1))
print([1.0,2.0,3.0]>[1,2,3])
print('python'>'python')
print({True,20,1}>{1,20})

# '<=' Operator
print(10<=22)
print((10,20)<=(20,10))
print([1,2,3]<=[1.0,2.0])
print('python'<='Python')
print({10,20}<={20,10,30})

# '>=' Operator
print(1000>=250)
print((1,3)>=(3,2,1))
print([1.0,2.0,3.0]>=[1,2,3])
print('Anaconda'>='python')
print({True,20,1}>={1,20,False})


print(not True and False or True)