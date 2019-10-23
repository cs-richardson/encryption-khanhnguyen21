'''
This program is used to encrypt text via Vigenere cipher
By Khanh Nguyen
'''
#Varibles

KEY = input('Key:') 
newKEY = KEY
checkNonLetter = False

#Check if key only contains alphabetical chacracters
for x in range (len(KEY)):
    letter = newKEY[x]
    letterNum = ord(letter)
    if letterNum < 65 and letterNum > 90 or letterNum < 97 and letterNum > 121 \
       or letter == ' ' or letter.isdigit() == True:
        checkNonLetter = True
        
if checkNonLetter == True or len(KEY) == 0:
    print('ERROR')
    
#Encryption process
else:
    #Functions
    #Convert letter into number/key
    def conversionKey(letter_number, initial_letter_number):
        key = letter_number - initial_letter_number
        return(key)

    #Convert the text with the key
    def conversionNormal(letter, initial_letter_number, key):
        delta = initial_letter_number - 1
        convertCipher = ( ( letter - delta + key ) % 26 )
        if convertCipher == 0:
            convertCipher = 26
        convertCipher = chr(convertCipher + delta)
        return(convertCipher)

    #The Encryption Logic
    def enLogic(y, letter, initial_letter, total):
        if ord(y) >= 65 and ord(y) <= 90:
            key = conversionKey(ord(y), ord('A'))
        else:
            key = conversionKey(ord(y), ord('a'))
        return( total + conversionNormal(letter, ord(initial_letter), key) )
    
    #The main process
    userInput = input('plain text:')
    total = ''
    loopTime = len(userInput) // len(KEY) + 1
    for x in range (loopTime):
        i = 0
        while(i < len(KEY)):
            try:
                y = KEY[i]
                letter = ord(userInput[:1])
            except:
                break
            userInput = userInput[1:]
            if letter < 65 or letter > 90 and letter < 97 or letter > 122:
                total = total + chr(letter)
            elif letter >= 65 and letter <= 90:
                total = enLogic(y, letter, 'A', total)
                i = i + 1
            else:
                total = enLogic(y, letter, 'a', total)
                i = i + 1      
    print('cipher text:', total)
