import sys, random
from decoder_module import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÜÑÍÓÉÁÚÇÈÏÛÔÎËÊÄÂ'

def main():
    myMessage = """I THOUGHT NOT. IT'S NOT A STORY THE JEDI WOULD TELL YOU. IT'S A SITH LEGEND. DARTH PLAGUEIS WAS A DARK LORD OF THE SITH, SO POWERFUL AND SO WISE HE COULD USE THE FORCE TO INFLUENCE THE MIDICHLORIANS TO CREATE LIFE... HE HAD SUCH A KNOWLEDGE OF THE DARK SIDE THAT HE COULD EVEN KEEP THE ONES HE CARED ABOUT FROM DYING. THE DARK SIDE OF THE FORCE IS A PATHWAY TO MANY ABILITIES SOME CONSIDER TO BE UNNATURAL. HE BECAME SO POWERFUL... THE ONLY THING HE WAS AFRAID OF WAS LOSING HIS POWER, WHICH EVENTUALLY, OF COURSE, HE DID. UNFORTUNATELY, HE TAUGHT HIS APPRENTICE EVERYTHING HE KNEW, THEN HIS APPRENTICE KILLED HIM IN HIS SLEEP. IT'S IRONIC HE COULD SAVE OTHERS FROM DEATH, BUT NOT HIMSELF."""
    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZÜÑÍÓÉÁÚÇÈÏÛÔÎËÊÄÂ'
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

    checkValidKey(myKey)

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        print(keyList)
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol

    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


if __name__ == '__main__':
    main()