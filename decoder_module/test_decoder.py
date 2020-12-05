import pytesseract as tesseract
import detectEnglish, vigenereCipher, pyperclip
tesseract.pytesseract.tesseract_cmd= r'C:\Users\grant\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image


def handwritten_to_string(file_path):
    input_string = tesseract.image_to_string(Image.open(file_path))
    input_string = input_string[:-1].strip()
    print(input_string)
    return input_string

def crack_ceasar(string):
        # message = 'GUVF VF ZL FRPERG ZRFFNTR.'#This is here for testing purposes
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÜÑÍÓÉÁÚÇÈÏÛÔÎËÊÄÂ'  # This is the alpahabet that will be used for the ceaser cipher 
        final_output = ''#String to store outputs and then be returned at good
        fo = open(r"C:\Users\grant\Documents\GitHub\Cerebro\decoder_module\dictionary.txt",encoding='utf8')
        words = fo.readlines()
        fo.close()
        for key in range(len(LETTERS)):     #Loops through each alpahbet combination to crack cipher
            translated = ''
            for symbol in string:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)  #This handles exceptions for symbols in the input string
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                    if detectEnglish.isEnglish(translated, wordPercentage=30):      #Detects to see if word is in dictionary and if the it is the same length as the input and then will add to output        
                        if len(translated)==len(string):                             
                            final_output += translated + '\n'
                else:
                    translated = translated + symbol
        if final_output!='':
            return final_output
        if final_output=='':# 
            return "There was no crack found. Ensure that you are correctly copying your cipher."
##########################################################################################################################################################
crack_ceasar("SUXHED")#THIS IS WHAT YOU CALL TO RUN THE CEASAR METHOD
##########################################################################################################################################################
handwritten_to_string(r"C:\Users\grant\Documents\GitHub\Cerebro\administrative_module\Spanish_ceasar_test.png")