from function_of_database import *



def open_database():
    database_name  = input("Enter the name of data base you want to open: ")
    print('_'*100)
    print()
    if isavaliable(database_name):
        print(f"Opening the Data Base of {database_name}")
        print('''
                1. Add Record
                2. Delete Record
                3. Find Record
                4. View All Record
                5. delete All Records
    ''')
        print('_'*100)

        choice = input("Enter your choice: ")
        print()
        
        if choice == '1':
            print('*'*100)
            print("Start Entring the DATA!")
            print('*'*100)
            print()
            add_record(database_name)
            print('*'*100)
        
        elif choice == '2':
            
            print('*'*100)
            del_record()
            print('*'*100)
        
        elif choice == '3':
            print('*'*100)
            find_record(database_name)
            print('*'*100)
        
        elif choice == '4':
            print('*'*100)
            Veiw_all_record(database_name)
            print('*'*100)
        
        elif choice == '5':
            print('*'*100)
            del_all_record(database_name)
            print('*'*100)
        else:
            print('*'*100)
            print("Invalid Choice")
            print('*'*100)
        
    else:
        print("No data Base is found with name","!"*30)
