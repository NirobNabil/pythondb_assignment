from user import User
from member import Memebr

while True:
    print("\nWelcome to BCU Lib System")
    uid = input("Enter uid: ")
    pswd = input("Enter your password: ")
    result = User.login(uid, pswd)
    if result['IsExist'] == True:
        print(f"Welcome {result['Name']}....")
        if result['Role'] == 'member':
            m = Memebr(result['Id'])
            m.menu()
            
    else:
        print("Login failure")
