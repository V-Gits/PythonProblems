"""
Write a Python program to implement Caesar cipher encryption and decryption
on a string of lowercase letters. Take distance value and the string as input. (Hint:
Caesar cipher encryption strategy replaces each character in the plaintext with the
character that occurs a given distance away in the sequence.
"""

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""  
    for char in text:
        if char.isalpha():
            if mode == "encrypt": 
                shift_value = shift  
            else:
                shift_value = -shift
            new_char = chr(((ord(char) - ord('a') + shift_value) % 26) + ord('a'))
            result += new_char
        else:
            result += char  
    return result


text = input("Enter the lowercase text: ")
shift = int(input("Enter the shift value: "))

encrypted_text = caesar_cipher(text, shift, "encrypt")
print("Encrypted Text:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, shift, "decrypt")
print("Decrypted Text:", decrypted_text)


#OutPut

"""
Enter the lowercase text: hello
Enter the shift value: 5
Encrypted Text: mjqqt
Decrypted Text: hello
"""