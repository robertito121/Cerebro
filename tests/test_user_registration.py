from administrative_module.cognito import CognitoUser

username = ""
password = ""  # password policy is min_length = 8 with numbers, special char, uppercase and lowercase
email = ""
first_name = ""
middle_name = ""
last_name = ""
phone_number = ""  # has to be in this format "+15555555555"
cognito = CognitoUser()
cognito.register_user(username, password,email, first_name, middle_name, last_name, phone_number)

