import pytesseract as tesseract
from PIL import Image


class OCR:

    @staticmethod
    def handwritten_to_string(self, file_path):
        input_string = tesseract.image_to_string(Image.open(file_path))
        input_string = input_string[:-1].strip()
        return input_string
