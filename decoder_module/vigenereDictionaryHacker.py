# Vigenere Cipher Dictionary Hacker

# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish, vigenereCipher, pyperclip

def main():
    ciphertext = """Hpüso isä aít áov xçdlë"""
    hackedMessage = hackVigenere(ciphertext)
   
def hackVigenere(ciphertext):
    fo = open(r"C:\Users\grant\Documents\GitHub\Cerebro\decoder_module\dictionary.txt", encoding="utf8")
    words = fo.readlines()
    fo.close()
    final_return=''
    for word in words:
        word = word.strip() # remove the newline at the end
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=100):
            # Check with user to see if the decrypted key has been found.
            #print('Key ' + str(word) + ': ' + decryptedText[:100])
            final_return+='Key ' + str(word) + ': ' + decryptedText[:100]+' '
    #return final_return #This is to be uncommented when the time is up
if __name__ == '__main__':
    main()