import threading
from threading import *
import time

library = {}

def manual():
    print("Hello User.")
    print()
    print("To access the library, we have a set of rules to be followed")
    print("1. For creating a record use, db.create_record(key,value,ttlvalue). ")
    print("2. For reading/accessing a record use, db.read_record(key) .")
    print("3. For deleting a record use, db.delete_record(key) .")
    print()
    print("For creating a record, specifying ttlvalue is optinal. If you do not need it, you can enter 0 in ttlvalue field.")
    print("While creating a record, check if the key already exists by checking the library, using the read_record(key) functionality.")
    print("While creating a record, note that the key should not exceed 32 bits, and the value should not exceed 16KB.")
    print()
    print("Now you are good to go.")



def read_record(key): #Specify the key here, so that library will search for the matching value and will display back.
    if(key in library):
        content = library[key]
        timetolive = content[1]
        if(timetolive != 0):
            if(time.time() < timetolive):
                jsonformat = str(key)+":"+str(content)
                return jsonformat
            else:
                print("ERROR : Time to live value has ended for this key.")
        else:
            jsonformat = str(key)+":"+str(content)
            return jsonformat

    else:
        print("ERROR : Key not present in library. Try a valid name.")



def create_record(key,value,ttlvalue): #Specify the key, value and ttlvalue for the record to create a new record
    if(key in library):
        print("ERROR : Key already exists in library.")
    else:
        if(key.isalpha()):
            if(len(library) < 1024**3):
                if(value <= 16*(1024**2)):
                    if(ttlvalue==0):
                        record = [value,ttlvalue]
                    else:
                        record = [value,time.time()+ttlvalue]
                    if(len(key) <= 32):
                        library[key] = record
                        print("Record successfully inserted")
                        print(key,":",value)
                else:
                    print("ERROR : Content size should not be more than 16KB")
            else:
                print("ERROR : Library is currently full - 1GB reached.")
        else:
            print("ERROR : Key should only contain alphabets.")


def delete_record(key): #Specify the key and the respective record will be deleted from the library.
    if(key in library):
        content = library[key]
        ttlvalue = content[1]
        if(ttlvalue != 0):
            if(time.time() < ttlvalue):
                del library[key]
                print("MESSAGE : Key deleted.")
            else:
                print("ERROR : Time to live value has ended for this key.")
        else:
            del library[key]
            print("MESSAGE : Key deleted.")
    else:
        print("ERROR : Enter a valid key.")



 
        
