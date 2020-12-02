import pytesseract as tesseract
tesseract.pytesseract.tesseract_cmd= r'C:\Users\grant\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
from PIL import Image
from langdetect import detect
#img=Image.open(r"C:\Users\grant\Documents\GitHub\Cerebro\administrative_module\untitled.png")
#text=tesseract.image_to_string(img)
#print(text)
      
def ocr(image_file_path):#Grant's Module
#This function will handle the image character recognition and storage
    input_string = tesseract.image_to_string(Image.open(image_file_path))#This converts the picture into a string
    input_string=input_string[:-1].strip()
    return input_string

#ocr(r"C:\Users\grant\Documents\GitHub\Cerebro\administrative_module\untitled.png")

def crack(ocr_string):
    #message = 'GUVF VF ZL FRPERG ZRFFNTR.'#This is here for testing purposes
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'#This is the alpahabet that will be used for the ceaser cipher
    final_output=''
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in ocr_string:    
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol 
        
        print('Key #%s: %s' % (key, translated)) #This is for test printing
        final_output+=translated+'\n'
    #print(final_output)
    return final_output
        
        
crack(ocr(r"C:\Users\grant\Documents\GitHub\Cerebro\administrative_module\untitled.png"))
