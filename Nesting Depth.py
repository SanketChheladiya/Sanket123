# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:03:55 2020

@author: Admin
"""
k=int(input())
for w in range(k):
    a=[0]
    an=[]
    n=input()
    l=list(n)
    for i in range(len(l)):
        d=int(l[i])
        a.append(d)
    a.append(0)
    for e in range(len(a)-1):
        temp=a[e]
        temp1=a[e+1]
        diff=temp-temp1
        if diff<0:
            for q in range((-(diff))):
                an.append("(")
        else:
            for q in range(diff):
                an.append(")")
        if e < len(l):
            an.append(l[e])
    str=""
    s=str.join(an)
    print("Case #{}: {}".format(w+1,s))
