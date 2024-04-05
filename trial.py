import pyrebase

config={
    'apiKey': "AIzaSyCpXh9kTgdstHO-eIE1DR8CLMC_x2fA6ww",
    'authDomain': "auth-student-analyzer.firebaseapp.com",
    'projectId': "auth-student-analyzer",
    'storageBucket': "auth-student-analyzer.appspot.com",
    'messagingSenderId': "282947312527",
    'appId': "1:282947312527:web:d492506ecad879288e49fa",
    'databaseURL':''
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()


email="test1@gmail.com"
password="123456"
# user=auth.create_user_with_email_and_password(email,password)
# print(user)

user=auth.sign_in_with_email_and_password(email,password)
print(user['email'])