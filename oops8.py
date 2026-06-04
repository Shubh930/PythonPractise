class Phone:
    def phone(self):
        print("used to talk ! ")
        
class Samsung(Phone):
    def samsung(self):
        print("used to take better selfie !")

class Iphone(Phone):
    def iphone(self):
        print("provides best security !")
        
obj = Iphone()
obj.iphone()
obj.phone()


