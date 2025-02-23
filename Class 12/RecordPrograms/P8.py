import pandas as pd
import numpy as np
print("Basic Arithmetic Operations with")
print("1.Same Index")
print("2.Different Index")
ch = int(input("Enter your choice:"))
if ch==1:
    n = int(input("Enter the number of elements in the 2 series: "))
    s1 = pd.Series(np.random.randint(0,100,n))
    s2 = pd.Series(np.random.randint(0,100,n))
    print(s1)
    print(s2)
    print("Arithmetic Operations with same index")
    print("Addition:")
    print(s1+s2)
    print("Subtraction:")
    print(s1-s2)
    print("Multiplication:")
    print(s1*s2)
    print("Division:")
    print(s1/s2)
elif ch==2:
    n = int(input("Enter the number of elements in the 2 series: "))
    s1 = pd.Series(np.random.randint(0,100,n),index = list(np.random.randint(0,100,n)))
    s2 = pd.Series(np.random.randint(0,100,n),index = list(np.random.randint(0,100,n)))
    print(s1)
    print(s2)
    print("Arithmetic Operations with different index")
    print("Addition:")
    print(s1+s2)
    print("Subtraction:")
    print(s1-s2)
    print("Multiplication:")
    print(s1*s2)
    print("Division:")
    print(s1/s2)
else:
    print("Invalid Choice!")