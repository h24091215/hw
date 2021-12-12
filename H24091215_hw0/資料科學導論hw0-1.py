# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 00:14:42 2021

@author: ASUS
"""


B=input('請輸入多項式:')
B1=B.strip('(')
B2=B1.strip(')')
polynomial=B2.split(')(')
#print(polynomial)

list1=[]
list2=[]
ans=[str(1)]
for i in polynomial:
    elements=i.split('+')
    list1.append(elements)
    #elements=i.split('-')
for i in list1:
    list3=[]
    for j in i:
        if '-' in j:
            j=j.split('-')
            t=len(j)
            list3.append(j[0])
                        
            for k in range(1,t):
                list3.append('-'+j[k])
        else:
            list3.append(j)
    list2.append(list3)
#print(list2)


def cross(variable1,variable2):
    if '*' in variable1:
        variable1=variable1.split('*')
        if '*'in variable2:
            variable2=variable2.split('*')
            number=int(variable1[0])*int(variable2[0])
            if variable1[1]==variable2[1]:
                A=str(int(number))+'*'+str(variable1[1])
            elif variable1[1]!=variable2[1]:
                A=str(int(number))+'*'+str(variable1[1])+str(variable2[1])
        elif '*' not in variable2:
            if variable2.isdigit():
                A=str(int(variable1[0])*int(variable2))+'*'+str(variable1[1])
            else:
                A=str(int(variable1[0]))+'*'+str(variable1[1])+str(variable2)
    else:
        if '*' in variable2:
            variable2=variable2.split('*')
            if variable1.isdigit():
                A=str(int(variable1)*int(variable2[0]))+'*'+str(variable2[1])
            else:
                A=str(int(variable2[0]))+'*'+str(variable1)+str(variable2[1])
        elif '*' not in variable2:
            if variable1.isdigit():
                if variable2.isdigit():
                    A=str(int(variable1)*int(variable2))
                else:
                    A=str(int(variable1))+'*'+str(variable2)
            else:
                if variable2.isdigit():
                    A=str(int(variable2))+'*'+str(variable1)
                else:
                    A=str(variable1)+str(variable2)
    return A

for i in list2:
    C=[]
    for k in i:
        for j in ans:
            #print(k,j,cross(k,j))
            C.append(cross(k,j))
    ans=C
#print(ans)

D=[]
for i in ans:
    if '*' in i:
        i=i.split('*')
        D.append(i[1])
print(D)
        
d1={}
for f in D:
    d={}
    for i in range(len(f)):
        if f[i].isalpha():
            if i==len(f)-1:
                if f[i] in d.keys():
                    d[f[i]]=int(d[f[i]])+1
                else:
                    d[f[i]]=1 
            elif f[i+1]=='^':
                if f[i] in d.keys():
                    d[f[i]]=int(d[f[i]])+f[i+2]
                else:
                   d[f[i]]=f[i+2] 
            else:
                if f[i] in d.keys():
                    d[f[i]]=int(d[f[i]])+1
                else:
                    d[f[i]]=1
    d1.setdefault(f,d)
print(d1)

d2=[]
for i in d1:
    for j in i:
        print(str(j)+str(int(d1[i][j])))
        #d2.append(str(j)+str(int(d1[i][j])))
    #print(d2)
