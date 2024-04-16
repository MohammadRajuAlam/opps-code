class Father:
    country="india"
    code="+91"

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def get_father(self):
        self.car="yes"
        print(f"Name: {self.name}\nAge: {self.age}\nSex: {self.sex}\n")

    def __account(self): # This is private function
        self.acc="12345678"
        self.__pswd="trg5678" # This is private variable
        self.acc_type="Saving"
        self.balance=568955
        print(f"Account No: {self.acc}\nPasword: {self.__pswd}\nAccount Type: {self.acc_type}\nBalance: {self.balance}\n")

    def get_acc(self):
        return self.__account()

    @classmethod
    def get_contry(cls):
        print(f"Country Name: {cls.country}\nCountry Code: {cls.code}\n")

    @staticmethod
    def get_address(village,city,pincode,district,state):
        print(f"Village Name: {village}\nCity: {city}\nPincode: {pincode}\nDistrict: {district}\nState: {state}\n")

obj=Father("Rasid",65,"Male")
#obj.get_father()
#print(obj.mariad) # We can call instance method variable after call the instance method, We can't call direct instance method variable
#obj.__account() # We can't access private function outside class
#obj.get_acc()
#print(obj.acc)
#print(obj.__pswd) # can't access bcz __pswd is a private variable
#obj.get_contry()
#Father.get_contry()
#obj.get_address("hemanhalli","Bangalore",560072,"Electronic city","Karnataka")
Father.get_address("hemanhalli","Bangalore",560072,"Electronic city","Karnataka")
