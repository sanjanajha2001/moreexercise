list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16] 
i=0
p=[]
while i<len(list1):
    if list1[i] not in p: 
        p.append((list1[i]))
        j=0
        while j<len(list2):
            if list2[j] not in p:
                p.append((list2[j]))
            j=j+1    
    i=i+1
print(p)