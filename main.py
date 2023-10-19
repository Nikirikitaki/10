from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    pass

class Phone(Field):
    def __init__(self, value):
       
        if len(value) == 10 and value.isdigit() == True:
            self.value = value
        else:
            raise ValueError("Invalid phone number")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        
    def add_phone(self,phone):
        self.phones.append(Phone(phone))
        
    def remove_phone(self,phone):
        phone_str = str(phone)
        if phone_str in [str(p) for p in self.phones]:
            self.phones = [p for p in self.phones if str(p) != phone_str]
        else:
            print(f"No record {phone} ")
            
    def edit_phone(self,phone,new_phone):
        found_res = self.find_phone(phone)
        if found_res:
            self.remove_phone(phone)
            self.add_phone(new_phone)
        else:
            raise ValueError 
                    
    def find_phone(self,phone:str):
        for p in self.phones:
            if p.value == phone:
            
                return p
        
            
        return None

    def __str__(self):
        phone_numbers = ', '.join(str(phone) for phone in self.phones)
        return f'{self.name} - {phone_numbers}'

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}
    def add_record(self, record):
        self.__setitem__(record.name.value, record)
        
    def find(self, name):
        if name in self.data:
            return self.data[name]
        else:
            return None
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"No record {name} ")
            
        
        
if __name__ == '__main__':
    book = AddressBook()
    # jane_record = Record("Jane")
    # jane_record.add_phone("1234567890")
    # jane_record.add_phone("1231231233")
    # jane_record.add_phone("3332223331")
    # book.add_record(jane_record)
    John_record = Record("John")
    John_record.add_phone("1234567890")
    John_record.add_phone("5555555555")
    
    # jane = book.find("Jane")
    # found_phone = jane.find_phone("1234567890")
    # print(f"{jane.name}: {found_phone}")
    # print(jane)
    
    phone = John_record.find_phone("1234567890")
    print(phone)
    
    
    # for name, record in book.data.items():
    #     print(record)
