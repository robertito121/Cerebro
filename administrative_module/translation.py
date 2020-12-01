def translate():#Grant's storage module
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'#This section is used to brute force the code
        for key in range(len(LETTERS)):
           translated = ''
           for symbol in input_string:
              if symbol in LETTERS:
                 num = LETTERS.find(symbol)
                 num = num - key
                 if num < 0:
                    num = num + len(LETTERS)
                 translated = translated + LETTERS[num]
              else:
                 translated = translated + symbol#End of bruteforce
            if translated(lang="eng+fra+ger+ita"):#Breaks out of loop if there is a language hit
                final_output=translated
                break
            print('Hacking key #%s: %s' % (key, translated))#This is for testing
        with open('final_output.txt', 'w') as f:#This creates a file to store the input string into the folder that the application is installed
            f.write("final_output %d" % final_output)