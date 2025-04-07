f = open(".\\FileProblems\\TextFilesFolder\\NumberFile.txt")
sum = 0
for line in f:
    num = int(line.strip())
    sum+=num
print(f"{sum=}")