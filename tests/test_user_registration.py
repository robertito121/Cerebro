from administrative_module.cognito import CognitoUser
import os

user_pool_id = os.getenv("USER_POOL_ID")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
username = ""
password = ""  # password policy is min_length = 8 with numbers, special char, uppercase and lowercase
email = ""
first_name = ""
middle_name = ""
last_name = ""
phone_number = ""  # has to be in this format "+15555555555"
cognito = CognitoUser(user_pool_id=user_pool_id, client_id=client_id, client_secret=client_secret, username=username)
cognito.register_user(password,email, first_name, middle_name, last_name, phone_number)

