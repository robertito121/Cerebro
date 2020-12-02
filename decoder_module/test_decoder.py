import pytesseract as tesseract
import detectEnglish, vigenereCipher, pyperclip
tesseract.pytesseract.tesseract_cmd= r'C:\Users\grant\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image


def handwritten_to_string(file_path):
    input_string = tesseract.image_to_string(Image.open(file_path))
    input_string = input_string[:-1].strip()
    return input_string

def crack_ceasar(string):
        # message = 'GUVF VF ZL FRPERG ZRFFNTR.'#This is here for testing purposes
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # This is the alpahabet that will be used for the ceaser cipher
        final_output = ''
        fo = open(r"C:\Users\grant\Documents\GitHub\Cerebro\decoder_module\dictionary.txt")
        words = fo.readlines()
        fo.close()
        for key in range(len(LETTERS)):
            translated = ''
            for symbol in string:
                if symbol in LETTERS:
                    num = LETTERS.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
                for word in words:
                    word = word.strip() # remove the newline at the end
                    if detectEnglish.isEnglish(translated, wordPercentage=30):
                        print('Key #%s: %s' % (key, translated))  # This is for test printing
                        break
            final_output += translated + '\n'
        # print(final_output)
        return final_output
def crack_simple(self,string):
    x=1
def crack_vigenere(self,string):
    x=1
crack_ceasar("RK PB JRG KH RQ A JDPHV PRGH")
