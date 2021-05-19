list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
i=0
p=[]
while  i<len(list2):
    if  list2[i] in list1:
        p.append((list2[i]))
    i=i+1
p.sort()    
print(p)