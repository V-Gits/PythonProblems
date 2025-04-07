"""
Design a program will perform the follwoing Tasks
1.Recive the filename from the user, open the file for input, and input the text
2. Count the number of sentences in the file
3. Count the Words in the text
4. Count the Syllables in the text
5. Compute the Flesch Index
6. Compute the Grade Level Equivalent
7. Print these two values with the appropriate labels, as well as the counts from task2-4
"""

fileName = input("Enter the FileName: ")

inputFile = open(fileName, "r")
text = inputFile.read()

sentences = text.count('.')+text.count('?').text.count(':')+text.count(';')+text.count('!')

words = text.split()

syllables = 0
vowels = "aeiouAEIOU"
for word in words:
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

index = 206.835 - 1.015*(len(words)/sentences)-84.6*(syllables/len(words))
level  = round(0.39*(len(words)/sentences)+11.8*(syllables/len(words))-15.59)

print(f"The Flesh Index is: {index}")
print(f"The Grace Level Equivalent is: {level}")
print(f"{sentences} sentences")
print(f"{len(words)} words")
print(f"{syllables} syllables")