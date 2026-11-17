import json
import os
import datetime
x = datetime.datetime.now()
date = x.strftime("%d")
day = x.strftime("%b")
id = date +" "+ day

File_Name = 'Data.json'


def creating_file():
    if not os.path.exists(File_Name) or os.path.getsize(File_Name) == 0:
        with open(File_Name,'w')as f:
                json.dump([],f)
        

def reading_file():
    with open(File_Name) as f:
        data = json.load(f)
        return data
    


def Write_file(load_data):
    with open(File_Name,'w') as f:
        json.dump(load_data,f,indent=4)



def add_income(amount,description):
    load_data = reading_file()
    income = {
        "id":id,
        "amount": amount,
        "Type":"Income",
        "Description":description
    }
    load_data.append(income)
    Write_file(load_data)

def add_expense(amount,description):
    load_data = reading_file()
    expense = {
        "id":id,
        "amount":amount,
        "Type":"Expense",
        "Description":description
    }
    load_data.append(expense)
    Write_file(load_data)


def filter_data(id=None):
    load_data = reading_file()
    if id is None:
        return json.dumps(load_data,indent=4)
    else:
        matched_data = []
        for item in load_data:
            if id == item['id']:
                matched_data.append(item)
        
        return (json.dumps(matched_data,indent=4))


creating_file()


