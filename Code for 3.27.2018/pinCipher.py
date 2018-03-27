## pinCyper.py
## Author: nmessa
## This is a Julius Ceasar cipher for PIN numbers

#This function encrypts your PIN
def PINCypher(pin, shift):
    cypherText = ""
    #Add code here
    
    return cypherText   

#This function will calculate your encryption key based on your last name
def calcShift(name):
    #Add code here
    

#This function will decode an encryted PIN
def PINDecode(ePin, shift):
    #Add code here

    
#Test code
pin = input("Enter your 5 digit PIN: ")
name = input("Enter your last name: ")
shift = calcShift(name)
ePin = PINCypher(pin, shift)
print("Your encrypted PIN is", ePin)
oPin = PINDecode(ePin, shift)
print("Your original PIN was", oPin)
