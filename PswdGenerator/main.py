import PswdChecker
import PswdGenerator

while True :
    user_options = input('Enter 1 To check Password Strength ;  Enter 2 To Create  Password \n : ')
    if user_options in ['1' , '2']:
        break 
    else:
        print('Invalid Input! Please Enter 1 or 2')

if user_options == '1':
    pswd = input('Enter Your Password : ')
    result = PswdChecker.check_password(pswd)
    print(result)
else:
    pswd = PswdGenerator.generate_password()
    print("Generated Password : ", pswd)
