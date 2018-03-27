## cypher.py
## Author: nmessa
## This function will implement a Ceasar Cypher of a string

def cypher(plain, shift):
    cipher = ""
    #Add code here
    
    return cipher  

#This function will calculate your encryption key based on your last name
def calcShift(name):
    total = 0
    for ch in name:
        total += ord(ch)
    return total%25 + 1

#This function will decode encryted text
def eTextDecode(eText, shift):
    plainText = ""
    #Add code here
    
    return plainText

#Test code
plainText = input("Enter some text to encrypt: ")
name = input("Enter your last name: ")
shift = calcShift(name)
cipherText = cypher(plainText, shift)
print("Your encrypted text is", cipherText)
plainText = eTextDecode (cipherText, shift)
print("Your original text is", plainText)

