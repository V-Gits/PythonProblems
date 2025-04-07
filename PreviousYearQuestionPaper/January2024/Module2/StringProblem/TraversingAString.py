STRING = "HELLO WORLD"
i = 0
print("Using While Loop")
while i < len(STRING):
    print(STRING[i])
    i+=1

print("\n\nUsing For Loop")
for j in range(len(STRING)):
    print(STRING[j])


#OUTPUT
"""
Using While Loop
H
E
L
L
O

W
O
R
L
D


Using For Loop
H
E
L
L
O

W
O
R
L
D
"""