# -*- coding: utf-8 -*-
"""practical 4.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aSgurZBIZyDckwg3_IVaYR12Xf8gdDYS
"""

0#square brackets used
#mutable and ordered
l1=[1,2,3,4,5,6]
l1.append(7)
print(l1)

l1=[1,2,3,4,5,6]
l1.extend([8,9])
print(l1)

l1.insert(1,'h')
print(l1)

l1.pop(0)
print(l1)

l1.remove(9)
print(l1)

l1.clear()
print(l1)

a=['hello','an',1,3,5,6,'an']
b=a.index('an',2)
print(b)

b=a.count('an')
print(b)

b=a.copy()
b.append(1)
print(a)
print(b)

b=len(a)
print(b)

a=[1,2,3,4,5,6,7,8,9]
m = max(a)
print(m)

m=min(a)
print(m)

a.sort()
print(a)

a.reverse()
print(a)

a=[2,3,4,5,6,7,8]
b=a[2]            #slicing
print(b)

b=a[2:6:2]
print(b)

b=a[-1:-4:-1]
print(b)