from create_database import *
from open_database import *


if __name__ == '__main__':


    print("CLI DATABASE MANGMENT SYSTEM")



    print("""
    1. Create New Data Base
    2. Open Data Base
""")
   
    choice = input("Enter Your Choice: ")

    if choice == '1':
        create_new_database()
    if choice == '2':
        open_database()