'''
This program is used to encrypt text via Ceasar cipher
By Khanh Nguyen
'''
try:
    key = int(input('Key:'))
except:
    print('Error')
else:
    userInput = input('plain text:')
    length = len(userInput)
    total = ''
    #Cipher function
    def conversion(letter, initial_letter_number):
        delta = initial_letter_number - 1
        letter = letter - delta
        convertCipher = ( ( letter + key ) % 26 )
        if convertCipher == 0:
            convertCipher = 26
        convertCipher = chr(convertCipher + delta)
        return(convertCipher)
    
    #convert to ASCII and cipher
    for i in range (length):
        letter = ord(userInput[i])
        if letter < 65 or letter > 90 and letter < 97 or letter > 122:
            total = total + chr(letter)
        elif letter >= 65 and letter <= 90:
            total = total + conversion(letter, ord('A'))
        else:
            total = total + conversion(letter, ord('a'))

    
    print('cipher text:', total)
