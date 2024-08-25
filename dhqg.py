# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:45:56 2024

@author: Student
"""

a = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
b = a.split(", ")
for i in b:
    print(i)
c = a.replace('P. ', '').replace('Q. ', '').replace('Tp. ', '').split(", ")
for u in c:
    print(u)
