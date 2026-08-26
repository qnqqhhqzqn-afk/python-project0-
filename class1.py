class famly:


    def __init__(self,name,age,hope=None):

        self.name=name
        self.age=age
        self.__hope=hope


    def get_hope(self):

        return self.__hope
    
    hope=property(get_hope)

e1=famly("moh",22,"mari")

e2=famly("bussra",55)

print(e1.name,e1.age,e1.hope)

print(e2.name,e2.age)