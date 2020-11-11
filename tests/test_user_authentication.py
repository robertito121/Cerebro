from administrative_module.cognito import CognitoUser

username = ""
password = ""

cognito = CognitoUser()
is_authenticated = cognito.authenticate_user(username, password)
print(is_authenticated)