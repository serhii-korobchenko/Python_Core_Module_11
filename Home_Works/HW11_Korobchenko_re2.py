# BOT assistent
# CLI - Command Line Interface
#              Architecture :
#                   - command`s parser
#                   - command`s processing functions (handler) - in--> str out-->str
#                   - request-answear loop

# Input - dict(name: telephone number)
# Requirements:
#              - telephone number format: 0675223345 - 10 digits;
#              - bot undestands commands:
#                          - "hello" - answear: "How can I help you?"
#                          - "add' name telephone number" - save new contact
#                          - "change' name telephone number" - save new telephone number for existed contact
#                          - "phone' name" - show telephone number
#                          - "show all" - show all contacts (name telephone number)
#                          - "addnum' name telephone number" - add aditional tel number for certain contact
#                          - "del' name telephone number" - del tel number for certain contact
#new - V                   - "addbirth" name birthday - add date of birthday in data format
#new -                     - "nextbirth" name - show how many days left up to next birthday
#                          - "good bye" or "close" or "exit" - bot stops work and messege "Good bye!"
#
#
# Additional requirements_(module 10, 11):
#                  UserDict Class:
#                         -user has Book of Contacts (AddressBook Class): 
#                                 |__> records (Record Class): --> dict {Record.name.value: value}
#                                                              --> Name object - separated atribute
#                                                              --> Phone objects - separated atribute
#
#                                          |__> fields (Field Class):
#                                                      - required (Name Class) - only one
#                                                      - optional (Phone Class) - one or more
#new - V                                               - optional (Birthday Class) - only one 
#
#                AdressBook methods:

#                                - add_record --> add Record in self.data
#                                - del  record
#                                - edit record              
#                                - find record by fields
#new                             - iterator - return --> generator by records -N records for 1 step
#
#                                           Record methods: 
#                                                 - add  field Phone
#                                                 - del  field Phone
#                                                 - edit field Phone
#new -                                            - days_to_birthday
# 
#new                                               Phone methods:
#new                                                     - setter - check tel. num format (7777777777)
#
#new                                               Birthday methods:
#new                                                     - setter - check birthday format (28.05.1978)


from multiprocessing.sharedctypes import Value
import re
from collections import UserDict
from datetime import datetime, timedelta


class AddressBook (UserDict):
        
    def add_record(self, name, phone):
        
        self.phone = phone
        
        #Name.value = name
        #Phone.value = phone
        #self.data[Name.value] = [(Record.phone.value)]
        self.data[name] = Record()
        

class Field:
    pass

class Name (Field):
    
    value = None

class Phone (Field):
    
    def __init__(self, value) -> None:
        self.value = value
       
    

class Birthday (Field):
    
    def __init__(self) -> None:
        self.value = None
    


""" 
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if re.match(r"\d{2}.\d{2}.\d{4}", new_value):
            self.__value = new_value
        else:
            print('Birthday format does not fit! Try again!') """
    

class Record:
    
    def __init__(self) -> None:
        
        self.name = Name()
        self.phone = Phone(add_book.phone)
        self.birthday = Birthday()
        self.record_dict = {
                         'Name': self.name.value,
                         'Phone': [self.phone.value],
                         'Birthday': self.birthday.value
                         }
        
    def add_phone (self, name, phone):
        #add_book.data[name].append(phone)
        add_book.data[name].record_dict['Phone'].append(phone)
       
    def del_phone (self, name, phone):
        add_book.data[name].record_dict['Phone'].remove(phone)

    def edit_phone (self, name, new_phone):  
        add_book.data[name].record_dict['Phone'].clear()
        add_book.data[name].record_dict['Phone'].append(new_phone)

    def days_to_birthday (self, name):
        next_year_birthday = datetime(year=datetime.now().year + 1, month=add_book.data[name].record_dict['Birthday'].month, day=add_book.data[name].record_dict['Birthday'].day)
        difference = next_year_birthday - datetime.now()
        print(f'{difference} left until next birthday!')

class TelDoesNotMathFormatError(Exception):
    status = 0

class BirthdayDoesNotMathFormatError(Exception):
    status = 0

class NameDoesNotExistError(Exception):
    status = 0

class TryAgainError(Exception):
    status = 0

def command_parser (command): # command`s parser
    command_id = ''
    name = ''
    phone = ''
       
    parsered_list = command.split (" ")
    if len(parsered_list) == 1:
        command_id = parsered_list[0].lower() # make all letters small
    
    elif len(parsered_list) == 2:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
    elif len(parsered_list) == 3:
        command_id = parsered_list[0].lower()
        name = parsered_list[1]
        phone = parsered_list[2]
    else:
        print ("Number of arguments do not fit to reqirements. Please try again!")
        
    return command_id, name, phone

### Decorator
def input_error(func): # decorator
    
    def inner(*args, **kwargs):

        func(*args, **kwargs) 

        if TelDoesNotMathFormatError.status == 1: # added functional zone
            print('Give me name and phone please')
            TelDoesNotMathFormatError.status = 0
        elif NameDoesNotExistError.status == 1:
            print('Enter user name please')
            NameDoesNotExistError.status = 0
        elif TryAgainError.status == 1:
            print('Please, Try again!')
            TryAgainError.status = 0
        elif BirthdayDoesNotMathFormatError.status == 1:
            print('Please, Try again!')
            BirthdayDoesNotMathFormatError.status = 0

    return inner

### handlers:
def hello_func ():
    print('How can I help you?')

@input_error
def add_func (name, phone):   #1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            add_book.add_record(name, phone) ###2

            print ('Information has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

@input_error
def change_func (name, phone):    #1&2

    try:
        if name in add_book.data:
            if re.match(r"^[0-9]{10,10}$", phone):
                
                Record().edit_phone(name, phone) ### 2

                print ('Phone number has been changed successfully!')
            else:
                raise TelDoesNotMathFormatError
        
        else:
            raise NameDoesNotExistError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1 

    except NameDoesNotExistError:

        print('Name does not exist')
        NameDoesNotExistError.status = 1
    
@input_error
def phone_func (name):           #1&2

    try:

        if name in add_book.data:   ### 2
            #for key, value in add_book.data[name].record_dict.items():  ### 2
                #if key == name:
            mystring = ', '.join(map(str, add_book.data[name].record_dict['Phone']))
            print(f'Phone number assigned for requested name is: {mystring}')
        else:
            raise NameDoesNotExistError

    except NameDoesNotExistError:

        print('Name does not exist.') #  - decorator
        NameDoesNotExistError.status = 1

def show_func ():

    if len(add_book.data) == 0:
        print('Data Base is empty yet. Please add someone!')
    else:
        print('Data Base contains next contacts:')
 
        for key, value in add_book.data.items():                   ### 2
            mystring = ', '.join(map(str, value.record_dict['Phone']))
            if value.record_dict['Birthday']:

                print(f"Name : {key} | Telephone numbers: {mystring} | Birthday: {value.record_dict['Birthday'].strftime('%A %d %B %Y')}")
            else:
                
                print(f"Name : {key} | Telephone numbers: {mystring} ")
        
@input_error
def addnum_func (name, phone):   #1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            Record().add_phone(name, phone) ###2

            print ('Information has been added successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

@input_error
def del_func (name, phone):   #1&2

    try:
        if re.match(r"^[0-9]{10,10}$", phone):
            
            Record().del_phone(name, phone) ###2

            print ('Telephone number has been deleted successfully!')
        else:
            raise TelDoesNotMathFormatError

    except TelDoesNotMathFormatError:

        print("Telephone number does not match format - should be 10 digits")
        TelDoesNotMathFormatError.status = 1

    except ValueError:
        print("Number assigned for deletion does not exist!")
        TryAgainError.status = 1

@input_error
def birth_func (name, birthday):   #1&2

    try:
        
        if re.match(r"\d{2}.\d{2}.\d{4}", birthday):
            
            birthday_data_list  = birthday.split('.')
            #print("birthday_data_list", birthday_data_list)
            birthday_datatime = datetime(year=int(birthday_data_list[2]), month=int(birthday_data_list[1]), day=int(birthday_data_list[0])).date()
            #print("birthday_datatime", birthday_datatime)
            add_book.data[name].record_dict['Birthday'] = birthday_datatime


            print ('Birthday date has been added successfully!')
        
        else:
            raise BirthdayDoesNotMathFormatError

    except BirthdayDoesNotMathFormatError:

        print("You have to set date in next format: dd.mm.yyyy! ")
        BirthdayDoesNotMathFormatError.status = 1

    except KeyError:
        print("This contact does not exist! First - set up appropriate contact")
        TryAgainError.status = 1

    except ValueError:
        print("You have to set date in next format: 1-31.1-12.0000-9999!")
        TryAgainError.status = 1

@input_error
def nextbirth_func (name):   #1&2

    try:
        
            
        Record().days_to_birthday(name) ###2

        #print ('Telephone number has been deleted successfully!')
          

    except KeyError:
        print("This contact does not exist! First - set up appropriate contact")
        TryAgainError.status = 1

def good_buy_func ():
    print('Good bye!')
    return 'stop'

### MAIN BODY FUNCTION
def main():
    # create dict
    #print('create dict')
    global add_book
    add_book = AddressBook()

    commands_dict = {'hello': hello_func, 'add': add_func, 'change': change_func,\
         'phone': phone_func, 'show': show_func, 'good': good_buy_func,\
         'close': good_buy_func, 'exit': good_buy_func, 'addnum': addnum_func, 'del': del_func,\
         'addbirth': birth_func, 'nextbirth': nextbirth_func  }
    
    stop_flag = ''
      
    print ("Bot has been started!")
    while True:
        try:
            
            print('')

            if len(add_book) == 0: # Print_to_check_addressbook
                print(add_book)
            else: 
                for key, value in add_book.items():
                    print(f'Name: {key}, Record: {value.record_dict}')
            
            command = input("Please, put you command in Command line! (from 1 to 3 arguments): ")   
            command_id, name, phone = command_parser (command) # passing vars to another func

            for key, value in commands_dict.items():
                if command_id == key and name == '' and phone == '':
                    res = value()
                    stop_flag = res

                elif command_id == key and name.lower() == 'bay' and phone == '':
                    res = value()
                    stop_flag = res

                elif command_id == key and name.lower() == 'all' and phone == '':
                    res = value()
                        
                elif command_id == key and name != '' and phone == '':
                    res = value(name)

                elif command_id == key and name != '' and phone != '':
                    res = value(name, phone)

            if command_id not in commands_dict:
                print('I do not know this command!')
                                               
            if stop_flag == 'stop':
                break

        except TypeError:
            print('Unsuccessful operation. Please, try again')
        
if __name__ == '__main__':
    main()