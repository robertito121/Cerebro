from pycognito import Cognito
from helper_module.helper import Helper



class CognitoUser:
    USER_POOL_ID = ''
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    log = Helper.get_logger()

    def __init__(self):
        self.log.info("initializing CognitoUser")

    def register_user(self, username, password, email, first_name, middle_name, last_name, phone_number):
        is_registered = False
        cognito = Cognito(self.USER_POOL_ID, self.CLIENT_ID,
                          client_secret=self.CLIENT_SECRET,
                          username=username)

        self.log.info("registering user with username " + username)
        try:

            cognito.set_base_attributes(email=email,
                                        given_name=first_name,
                                        middle_name=middle_name,
                                        family_name=last_name,
                                        phone_number=phone_number)
            cognito.register(username=username, password=password)
            is_registered = True
            self.log.info("username " + username + " registered successfully")
        except Exception as e:
            if "UsernameExistException" in str(e):
                self.log.error("Username already exist, please user another username")
            else:
                self.log.error(str(e))
        return is_registered

    def confirm_signup(self, username, confirmation_code):
        signup_confirmed = False
        cognito = Cognito(self.USER_POOL_ID, self.CLIENT_ID,
                          client_secret=self.CLIENT_SECRET,
                          username=username)
        self.log.info("confirming user=" + username + " with registration code " + confirmation_code)
        try:
            cognito.confirm_sign_up(confirmation_code, username=username)
            signup_confirmed = True
            self.log.info("user = " + username + " has been confirmed ")
        except Exception as e:
            self.log.error(str(e))
        return signup_confirmed

    def authenticate_user(self, username, password):
        is_authenticated = False
        cognito = Cognito(self.USER_POOL_ID,
                          self.CLIENT_ID,
                          client_secret=self.CLIENT_SECRET,
                          username=username)
        self.log.info("Authenticating user = " + username)
        try:
            cognito.authenticate(password=password)
            is_authenticated = True
            self.log.info("user = " + username + " has been authenticated")
        except Exception as e:
            self.log.error(str(e))
        return is_authenticated
    ##########################################################################################################################
    ###GRANTS SECTION###GRANTS SECTION###GRANTS SECTION###GRANTS SECTION###GRANTS SECTION###GRANTS SECTION###GRANTS SECTION###
    ##########################################################################################################################
    try: #Yeah this will be moved to the top
        from PIL import Image #Imports the necessary files to get pytesseract to work#
    except ImportError:
        import Image
    import pytesseract    
        
    def ocr(image_file):#Grant's Module
    #This function will handle the image character recognition and storage
        input_string = pytesseract.image_to_string(Image.open(imgage_file))#This converts the picture into a string
        with open('input_string.txt', 'w') as f:#This creates a file to store the input string into the folder that the application is installed
            f.write("input_string %d" % input_string)
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
        