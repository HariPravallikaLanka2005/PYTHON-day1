"""
Logical operators mean they just perform logical operations
Logical AND : if both the values are true it returns the true
Logical OR  : if one of the value is true it returns the true
Logical NOT : just negotiates the condition

a  b  aandb   a  b  aorb     a  not(a)
T  T  T       T  T  T        T  F
T  F  F       T  F  T        F  T
F  T  F       F  T  T
F  F  F       F  F  F  
"""
a = 23
b = 34
c = a!=b and b>a #T and T -- T
print(c)

d = "ece"
e = "5g"
f = d!="5g" or d=="ece"# F or T--T
print(f)

a = 1 #True 
print(not(a)) # False

a=0 #False
print(not(a)) #True