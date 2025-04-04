NUM = int(input("Enter the Number of Terms: "))
if NUM <= 0:
    pass
elif NUM == 1:
    print(0)
elif NUM == 2:
    print(0,1)
else:
    li = [0,1]
    i = 2
    while i < NUM:
        li.append(li[i-1] + li[i-2])
        i += 1
    print(li)