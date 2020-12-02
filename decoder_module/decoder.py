from digital_processing_module.digital_processing import OCR


class Decoder:

    @staticmethod
    def crack(self, string):
        # message = 'GUVF VF ZL FRPERG ZRFFNTR.'#This is here for testing purposes
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # This is the alpahabet that will be used for the ceaser cipher
        final_output = ''
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

            print('Key #%s: %s' % (key, translated))  # This is for test printing
            final_output += translated + '\n'
        # print(final_output)
        return final_output


Decoder.crack(OCR.handwritten_to_string(r"C:\Users\grant\Documents\GitHub\Cerebro\administrative_module\untitled.png"))
