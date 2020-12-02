from administrative_module.cognito import CognitoUser
import os

user_pool_id = os.getenv("USER_POOL_ID")
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
username = ""
password = ""

cognito = CognitoUser(user_pool_id=user_pool_id, client_id=client_id, client_secret=client_secret, username=username)

user = cognito.get_user_info(password)
print(user.__getattr__('first_name'))

