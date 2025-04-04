"""
Write Python code for the following statements
i) Write the text "PROGRAMMING IN PYTHON" to a file name code.txt
ii) then reads the text again and prints it to the screen.
"""

f = open("code.txt", "w")
f.write("PROGRAMMING IN PYTHON")
f.close()

f = open("code.txt", "r")
print(f.read())
