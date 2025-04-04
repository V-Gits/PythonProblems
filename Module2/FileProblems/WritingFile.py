import random
f = open(".\\FileProblems\\TextFilesFolder\\RandomIntegers.txt", "w")
for i in range(100):
    f.write(str(random.randint(1, 100)) + "\n")
f.close()