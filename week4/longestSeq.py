string =list(map(int,input("Enter the input: ").split()))
c=[]
for i in string:
    b=1
    k=i+1
    for j in string:
        if k in string:
            b+=1
            k+=1
    c.append(b)
print(max(c))