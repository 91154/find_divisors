n = int(input("enter a noumber : "))

i = 1
l=[ ]
while i <= n:
    if n % i == 0:
        l.append(i)

    i +=1
print(l)