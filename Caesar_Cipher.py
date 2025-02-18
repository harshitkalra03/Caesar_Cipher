"""
Owner:- Harshit Kalra
Date:- 18-02-2025
Agenda:- In this project, I am going to develop a program to cipher and decipher a program based upon the 
tradionally used concept in cryptography of cipher and decipher a string by using a shift key, for security reasons .
"""


from art import Welcome_Portal
print(Welcome_Portal)

alphabets = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 
 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, 'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 
 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 
 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}


service = input("What type of service you want from the portal, cipher or decipher?\n").lower()

def cipher(string, shift):
    cipher_text = ""
    for i in range(len(string)):
        cipher_text += [key for key, value in alphabets.items() if value == (alphabets[string[i]]+shift)%52][0]
    return cipher_text
    
def decipher(string, shift):
    decipher_text = ""
    for i in range(len(string)):
        decipher_text += [key for key, value in alphabets.items() if value == (alphabets[string[i]]-shift)%52][0]
    return decipher_text
    
if service=="cipher":
    text = input("Enter the string which you want to cipher.\n")
    key = int(input("What is your shift key?\n"))
    print(f"The ciphered text for {text} in lower cases is {cipher(string = text, shift = key)}.")

elif service=="decipher":
    text = input("Enter the string which you want to decipher.\n")
    key = int(input("What is your shift key?\n"))
    print(f"The deciphered text for {text} in lower cases is {decipher(string = text, shift = key)}.")

else:
    print("There is no such service available, please recheck the list of available services.")