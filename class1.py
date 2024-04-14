class Father:
    national="India"
    code="+91"
    def __init__(self,name,age,shop):
        self.name=name
        self.age=age
        self.shop=shop
        
    def get_father(self):
        print(f"This is Belong to Father instance method\nName:{self.name}\nAge: {self.age}\nNo of Shops: {self.shop}\n")

    def get_f_account(self):
        self.b_name="PNB"
        self.account=4578694
        self.__pasword="erhfiiof45"
        self.type="Saving"
        self.balance=150000
        print("Father Bank Account Details")
        print(f"Bank Name: {self.b_name}\nAccount No: {self.account}\nAccount Type: {self.type}\nBalance: {self.balance}\n")
        
    @classmethod
    def get_national(cls):
        print(f"Nationality: {cls.national}\nCode: {cls.code}\n")

    @staticmethod
    def get_f_address(city,state,pincode,phone):
        print(f"City: {city}\nState: {state}\nPincode: {phone}\n")
        
class Mother:
    mob=8892341236
    email="abida6@gmail.com"
    def __init__(self,name,age,bike):
        self.m_name=name
        self.m_age=age
        self.bike=bike
        print("This is Mother Constructor")
        #super().__init__("Abida",55,3)
    def get_mother(self):
        print(f"This is instance class of Mother\nName: {self.m_name}\nAge: {self.m_age}\nNo of Bike: {self.bike}\n")

    @classmethod
    def get_m_address(cls):
        print("Mother's Mobile")
        print(f"Mobile: {cls.mob}\nEmail: {cls.email}\n")

    @staticmethod
    def get_m_acc(name,acc,acc_type,balance):
        print("Mother Bank Details")
        print(f"Bank Name: {name}\nAccount No: {acc}\nAccount Type: {acc_type}\nBalance: {balance}")

class Child(Father,Mother):
    last_qua="BCA"
    passout=2015
    def __init__(self,name,clas,roll,):
        self.name=name
        self.clas=clas
        self.roll=roll
        super().__init__("Abdul",62,3) # Here Calling Father class using super() OR
        #Father.__init__(self,"Abdul",62,3) # We can also call Father class using using class name like Father
        Mother.__init__(self,"Amina",55,1) # Here calling Mother class using class name like Mother
        
    def get_child(self):
        print(f"Name: {self.name}\nClass: {self.clas}\nRoll No: {self.roll}\n")

    @classmethod
    def get_last_quali(cls):
        
        print(f"Last Qualification: {cls.last_qua}\nYear of Passout: {cls.passout}\n")

    @staticmethod
    def get_college(c_name,add,city,phone,email):
        print(f"College name: {c_name}\nAddress: {add}\nCity: {city}\nPhone: {phone}\nEmail: {email}\n")
        

obj3=Child("Alam","BCA","1AMBCA15")
# Here Accessing for child class
#obj3.get_child()
#obj3.get_last_quali()
#Child.get_last_quali()
#obj3.get_college("Cryst university","Bangalore Near Dairy Circle","Bangalore",8955756331,"cryst@gmail.com")
#Child.get_college("Cryst university","Bangalore Near Dairy Circle","Bangalore",8955756331,"cryst@gmail.com")

# Here Accessing Mother class
#obj3.get_mother()
#obj3.get_m_address()
#Child.get_m_address()
#obj3.get_m_acc("BOI",1254869871,"Saving",540000)
#Child.get_m_acc("BOI",1254869871,"Saving",540000)


# Here Accessing Mother class
#obj3.get_father()
#obj3.get_f_account()
#obj3.get_national()
#Child.get_national()
obj3.get_f_address("get_f_address","Karnataka",560029,993465789)





