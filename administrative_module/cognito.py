from pycognito import Cognito


class CognitoUser:

    USER_POOL_ID = ""
    CLIENT_ID = ""
    CLIENT_SECRET = ""

    def __init__(self):
        print("initializing CognitoUser")

    def register_user(self, username, password, email, first_name, middle_name, last_name, phone_number):
        is_registered = False
        cognito = Cognito(self.USER_POOL_ID, self.CLIENT_ID,
                          client_secret=self.CLIENT_SECRET,
                          username=username)
        try:

            cognito.set_base_attributes(email=email,
                                        given_name=first_name,
                                        middle_name=middle_name,
                                        family_name=last_name,
                                        phone_number=phone_number)
            cognito.register(username=username, password=password)
            is_registered = True
        except Exception as e:
            if "UsernameExistException" in str(e):
                print("Username already exist, please user another username")
            else:
                print(e)

        return is_registered

    def confirm_signup(self, username, confirmation_code):
        signup_confirmed = False
        cognito = Cognito(self.USER_POOL_ID, self.CLIENT_ID,
                          client_secret=self.CLIENT_SECRET,
                          username=username)
        try:
            cognito.confirm_sign_up(confirmation_code, username=username)
            signup_confirmed = True
        except Exception as e:
            print(e)

        return signup_confirmed

    def authenticate_user(self, username, password):
        is_authenticated = False
        cognito = Cognito(self.USER_POOL_ID,
                          self.CLIENT_ID,
                          client_secret=self.CLIENT_SECRET,
                          username=username)
        try:
            cognito.authenticate(password=password)
            is_authenticated = True
        except Exception as e:
            print(e)
        return is_authenticated
