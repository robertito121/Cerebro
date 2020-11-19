from pycognito import Cognito
from helper_module.helper import Helper




#This class supports user regestration and user authentication

class CognitoUser:
    USER_POOL_ID = ''
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    log = Helper.get_logger()

    def __init__(self):
        self.log.info("initializing CognitoUser")
        # this method allows the registration of a user in AWS cognito
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
                #registration error handling
        except Exception as e:
            if "UsernameExistException" in str(e):
                self.log.error("Username already exist, please user another username")
            else:
                self.log.error(str(e))
        return is_registered
            #This method allows for the user to confirm registration
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
            # Error handling for user confirmation
        except Exception as e:
            self.log.error(str(e))
        return signup_confirmed
        #This method Authenticates the user upon sign in
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
            # Authentication Error Handling
        except Exception as e:
            self.log.error(str(e))
        return is_authenticated
