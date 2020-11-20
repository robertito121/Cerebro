from pycognito import Cognito
from helper_module.helper import Helper




#This class supports user regestration and user authentication

class CognitoUser:

    def __init__(self, user_pool_id, client_id, client_secret, username):
        self.user_pool_id = user_pool_id
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.cognito = Cognito(user_pool_id, client_id, client_secret=client_secret, username=username)
        self.log = Helper.get_logger()

    # this method allows the registration of a user in AWS cognito
    def register_user(self, password, email, first_name, middle_name, last_name, phone_number):
        is_registered = False
        self.log.info("registering user with username " + self.username)
        try:
            self.cognito.set_base_attributes(email=email,
                                             given_name=first_name,
                                             middle_name=middle_name,
                                             family_name=last_name,
                                             phone_number=phone_number)
            self.cognito.register(username=self.username, password=password)
            is_registered = True
            self.log.info("username " + self.username + " registered successfully")
        except Exception as e:
            if "UsernameExistException" in str(e):
                self.log.error("Username already exist, please user another username")
            else:
                self.log.error(str(e))
        return is_registered

    #This method allows for the user to confirm registration
    def confirm_signup(self, confirmation_code):
        signup_confirmed = False
        self.log.info("confirming user=" + self.username + " with registration code " + confirmation_code)
        try:
            self.cognito.confirm_sign_up(confirmation_code, username=self.username)
            signup_confirmed = True
            self.log.info("user = " + self.username + " has been confirmed ")
        except Exception as e:
            self.log.error(str(e))
        return signup_confirmed

    def authenticate_user(self, password):
        is_authenticated = False
        self.log.info("Authenticating user = " + self.username)
        try:
            self.cognito.authenticate(password=password)
            is_authenticated = True
            self.log.info("user = " + self.username + " has been authenticated")
        except Exception as e:
            self.log.error(str(e))
        return is_authenticated
