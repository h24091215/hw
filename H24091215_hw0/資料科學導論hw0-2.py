# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 02:04:25 2021

@author: ASUS
"""
B=[]
f=open('C:/Users/ASUS/Downloads/IMDB-Movie-Data.csv','r',encoding='UTF-8')
for line in f:
    #print(line,end='')
    A=line.split(',')
    B.append(A)
    #print(A[7] in B)
#f.close()

#第一題
#[rate,name]
rate1=[0,0]
rate2=[0,0]
rate3=[0,0]
del B[0]#刪掉標題
for A in B:
    
    rate=float(A[7])
    #找到第一名
    if rate>rate1[0] and A[5]=='2016':
        rate1=(float(A[7]),A[1])
    #找到第二名
    elif rate>rate2[0] and A[5]=='2016':
        rate2=(float(A[7]),A[1])
    #找到第三名
    elif rate>rate3[0] and A[5]=='2016':
        rate3=(float(A[7]),A[1])
print('no.1:',rate1[1],'no.2:',rate2[1],'no.3',rate3[1])

#第二題
allrevenue={}
D=[]
for A in B:
    C=A[4].split('|')
    for i in C:
        if i not in D:
            D.append(i.lstrip())
    for i in D:
        allrevenue[i]=[]
for A in B:
    if A[9]!='':
        E=[]
        C=A[4].split('|')
        for i in C:
            E.append(i.lstrip())
        for i in E:
            p=allrevenue[i]
            p.append(float(A[9]))
            allrevenue[i]=p
        #print(E)
b=0
for i in D:
    if allrevenue[i]!=[]:
        a=sum(allrevenue[i])/len(allrevenue[i])
        if a>b:
            b=a
            c=i
print(c)
#print(allrevenue)
#print (D)

#第三題
emmarate=[]
for A in B:
    rate=float(A[7])
    C=A[4].split('|')
    D=[]
    for i in C:
        D.append(i.lstrip())
    if 'Emma Watson' in D:
        #print(rate)
        emmarate.append(rate)
print("average rating of Emma's movies:", sum(emmarate)/len(emmarate))

#第四題
director=[]
dict1={}
for A in B:
    if A[3] not in director:
        director.append(A[3])
a=0
b=0
c=0
for i in director:
    dict1[i]=[]
for A in B:
    E=[]
    dire=A[3]
    C=A[4].split('|')
    for i in C:
        E.append(i.lstrip())
    for j in E:
        if j not in dict1[dire]:
            dict1[dire].append(j)
for i in director:
    collaborate=len(dict1[i])
    if collaborate>a:
        a=collaborate
        first=i
    elif collaborate>b:
        b=collaborate
        second=i
    elif collaborate>c:
        c=collaborate
        third=i
print(first,second,third)

#第五題
D=[]
genre={}
for A in B:
    C=A[4].split('|')
    for i in C:
        if i.lstrip() not in D:
            D.append(i.lstrip())
            
for i in D:
    genre[i]=[]
    #print(genre)
for A in B:
    G=A[2].split('|')
   # print(G)
    E=[]
    C=A[4].split("|")
    for i in C:
        E.append(i.lstrip())
    for i in E:
        for j in G:
            if j not in genre[i]:
                genre[i].append(j)
#print(D)
#print(genre)
a=0
b=0
for i in D:
    gen=len(genre[i])
    if gen>a:
        b=a
        second=first
        a=gen
        first=i
        
    elif gen>b:
        b=gen
        second=i
print('first:',first)
for i in D:
    gen=len(genre[i])
    if gen==len(genre[second]):
        print('second:',i)
#print(D)            

#第六題
year={}
for i in D:
    year[i]=[]
#print(D)
for A in B:
    C=A[4].split('|')
    #print(A[5])
    E=[]
    for i in C:
        E.append(i.lstrip())
    for i in C:
        if i not in E:
            E.append(i.lstrip())
    for i in E:
        year[i].append(int(A[5]))

#print(year)
for i in D:
    gapyear=max(year[i])-min(year[i])
    if gapyear>a:
        a=gapyear
        first=i
print('first:',first)
for i in D:
    gapyear=max(year[i])-min(year[i])
    if gapyear==max(year[first])-min(year[first]) and i!=first:
        print('first:',i)


#第七題
s=set(['Johnny Depp'])

for A in B:
    E=[]
    C=A[4].split("|")
    for i in C:
        E.append(i.lstrip())
    for i in s:
        if i in E:
           s=s|set(E) 
           #print(s1)
    for i in E:
        if i in s:
           s=s|set(E)
for A in B:
    E=[]
    C=A[4].split("|")
    for i in C:
        E.append(i.lstrip())
    for i in s:
        if i in E:
           s=s|set(E) 
    for i in E:
        if i in s:
           s=s|set(E)
for A in B:
    E=[]
    C=A[4].split("|")
    for i in C:
        E.append(i.lstrip())
    for i in s:
        if i in E:
           s=s|set(E) 
    for i in E:
        if i in s:
           s=s|set(E)
for A in B:
    E=[]
    C=A[4].split("|")
    for i in C:
        E.append(i.lstrip())
    for i in s:
        if i in E:
           s=s|set(E) 
    for i in E:
        if i in s:
           s=s|set(E)

print(s)
    
    