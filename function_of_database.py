import json

def load_metadata(database_name):
    '''Take database Name which was created and return the meta data of that database'''

    with open(f"{database_name}_metadata.txt",'r') as file:
        return json.load(file)


def load_data(database_name):
    '''Take Database Name and check if file of that database avaliable than return Data from that data base or if file is not present return empty list because if we want to add data we can first extract the previously stored in file than manupuliate that data and save manupulative data'''
    try:
        with open(f"{database_name}.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(database_name,data):
    "Helps in dumping the data in file take database_name create file of that name and write data on that file"
    with open(f"{database_name}.txt",'w') as file:
            json.dump(data,file)

    
def load_DATABASES():
    '''Return all the Database Stored in a Main file named DATABASES '''
    try:
        with open("DATABASES.txt",'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def isavaliable(database_name):

    '''takes database name and retruns True if Data Base is present in main DATABASES file Otherwise False'''

    data=load_DATABASES()
    if len(data) > 0:
        for i in data:
            if i == database_name:
                return True
    return False



def add_record(database_name):
    '''It take the Database name as arguments load the meta data of that database and based on that meta data allow user to enter data accordingly and dump that data in file having name of that database'''

    metadata = load_metadata(database_name)
    record = load_data(database_name)

    while True:
        data ={}
        for i in metadata:
            item = input(f"{i['field']} :")
            
            data.update({i["field"]:item})
            
        record.append(data)
        # for stop entring the records
        x = input("press x to stop: ")  
        print('*'*100)
        print()
        if x == 'x':
            break  

    save_data_helper(database_name,record)
    print("DATA SAVE SucessFully","."*100)

def del_record(database_name):
    try:
        with open(f"{database_name}.txt",'r' ) as file:
            pass
    except FileNotFoundError:
        return []

# def choice_finding(choice,database_name):
#     record = load_data(database_name)
#     if choice =='1':
#         x = input("enterthe name of std:")
#         for dic in record:
#             for key,value in dic.items():
#                 if key == '':


def find_record(database_name):
    records = load_data(database_name)
    metadata = load_metadata(database_name)
    print("On Which attritude you want to find the record: ")

    dic_choice={}
    
    for index,dic in enumerate(metadata,start=1):
        dic_choice.update({index:f'{dic['field']}'}) # here i am assigning a numeric key to every field so that they can be accessed as dic is un ordred. Remember you can oly pass dic as an argument to update method.
        print(f"{index} : {dic['field']}")

    choice = int(input("Enter you choice: ")) 

    print('*'*100)
    # VERY VERY AMAZING LOGIC here i am choice will only be valid if it is equal or less than len of dic_choice cuz dic choice contain all the field name of database secondly i am extracting keys values and valus from dic_choice and checking at which keyof dic choice = choice of user than if they are equal i am asking user to enter the value which he want to find in his choiced attribuet then i am looping through all dic in the record and checking that any dic[value] of record == finding->(if key 2 == choice than acutually value of key == field in which you want to find the data and now you field name so you can iterate through all dic and find that the valu of that field is == to finding). if equal i am printing the entire record of that data.
    if choice <= len(dic_choice):
        for keys,values in dic_choice.items():
                if choice == keys:
                    finding = input(f"Enter The value you want to find in field of {values}: ")
                    for dic in records:
                        # try:
                            
                            if dic[values] == finding: #here value contain that field name which is chosen by user so for every dic in records for example value contain marks so for marks key in evey dic is being checked wheather it is  equal to what we are finding
                                print("Record is found.............")
                                for keys,values in dic.items():
                                    print(f"{keys} : {values}")
                                break
                        # except:
                            # print("Record not found")
                    else:
                        print("Sorry! Record Not Found.............")        
    else:
        print("Invalid Choice")
    
    print('*'*100)

    

    


def display_record(metadata,records):
        '''Takes Metadata and record. make a header varibale and store Field name extracting from metadata and use that header to etract the data from the record because the data in the dictories of record is get by dic['name_field'] in this case '''
        print('='*90)
        for dic in metadata:
            header = dic['field']
            print(f"{header} " ,end = ":")
            for dic in records:
                print(f"{dic[header]}", end =" ")
            print()
        print('='*90)

def Veiw_all_record(database_name):
    metadata = load_metadata(database_name)
    records = load_data(database_name)
    display_record(metadata,records)
    
    

def del_all_record(database_name):
    data = load_data(database_name)
    data = []
    save_data_helper(database_name, data)
    print("All the data is Deleted")
    Veiw_all_record(database_name)
