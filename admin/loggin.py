from database import *

collection = db['USERS']


def createAccount(mail:str, password:str):
    collection.insert_one({mail: password})

def loggin(mail:str, password:str):
    try:
        results = collection.find({})
        for r in results:
            if r[mail] == password:
                return True
            else:
                return False
            break
    except KeyError:
        createAccount(mail, password)
        return "NEW"
