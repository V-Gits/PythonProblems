NUM = int(input("Enter the Height for the Pyramid: "))
for row_num in range(NUM+1):
    row = [1] * row_num
    for i in range(1, row_num):
        row[i] = row[i-1]+row[i]
    line = " ".join(map(str,row))
    gap_num = NUM-row_num
    gap = " " * gap_num
    print(gap+line)