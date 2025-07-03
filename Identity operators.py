"""
Identity operators are used to compare the values and returns the boolean values.
The operators are "is","is not"
"""
X = [1,2,3]
Y = [4,5,6]
Z = X
print(X is Y)#F
print(X is Z)#T
print(Y is Z)#F
print(Y is not Z)#T
print(Z is not X)#F
print(X is not Y)#T