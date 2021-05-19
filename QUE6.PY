string = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
i=0
p=[]
while i<len(string):
    if string[i] not in p:
        p.append((string[i]))
    i=i+1
print(p)