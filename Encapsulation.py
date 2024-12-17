class t:
    def __init__(self,name,age):
        self.__name=name 
        self.__age=age
    
    def set_name(self,name,age):
       self.__name =name
       self.__age = age

    def get_name(self):
     return self.__name,self.__age
    

u= t("kanna",34)
print(u.get_name())
# y = t("kanna",23)
# print(y.get_name())

    