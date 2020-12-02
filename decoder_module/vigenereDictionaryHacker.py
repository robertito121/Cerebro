# Vigenere Cipher Dictionary Hacker

# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish, vigenereCipher, pyperclip

def main():
    ciphertext = """Fh ul hcz ye wa y uwdea zpra"""
    hackedMessage = hackVigenere(ciphertext)
    
    if hackedMessage != None:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    #else:
        #print('Failed to hack encryption.')
def hackVigenere(ciphertext):
    fo = open(r"C:\Users\grant\Documents\GitHub\Cerebro\decoder_module\dictionary.txt")
    words = fo.readlines()
    fo.close()
    final_return=''
    for word in words:
        word = word.strip() # remove the newline at the end
        decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
        if detectEnglish.isEnglish(decryptedText, wordPercentage=37):
            # Check with user to see if the decrypted key has been found.
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            final_return+='Key ' + str(word) + ': ' + decryptedText[:100]+' '
    return final_return
if __name__ == '__main__':
    main()