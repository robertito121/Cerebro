import pytesseract as tesseract
from PIL import Image
tesseract.pytesseract.tesseract_cmd= r'C:\Users\grant\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


class OCR:

    @staticmethod
    def handwritten_to_string(file_path): #
        input_string = tesseract.image_to_string(Image.open(file_path),lang='eng+fra+spa')
        input_string = input_string[:-1].strip()
        return input_string
