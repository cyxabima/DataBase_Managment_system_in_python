from function_of_database import *
import json

def create_new_database():

    dataBases_data = load_DATABASES()
    database_name = input("Enter the name of Data Base  you want to create: ")

    if  not isavaliable(database_name):
        database_file = f"{database_name}_metadata"
        metadata = []
        dataBases_data.append(database_name)

        while True:
            name_field = input("Enter the name of field or x to exit: ")
            if name_field  == 'x':
                break
            type_field = input(f"Enter the type for the {name_field}: ")
            
            metadata.append({"field" :name_field , "type": type_field})
            
        save_data_helper("DATABASES",data=dataBases_data)
        save_data_helper(database_file,data= metadata)

    else:
        print(f"{database_name} already Exist")