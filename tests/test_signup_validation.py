from administrative_module.cognito import CognitoUser

username = ""
registration_code = ""   # put registration code from email
cognito = CognitoUser()
cognito.confirm_signup(username, registration_code)