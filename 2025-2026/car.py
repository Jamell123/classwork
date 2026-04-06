#jamell coleman
#04-6-26




class Car:
    def __init__(self,name,model,color, year):
       self.name = name
       self.model = model
       self.color = color
       self.year = year



def main():
    kiatelluride=Car( "kia ","telluride" ,"grey", 2008)
    print(kiatelluride.name)
    print(kiatelluride.model)
    print(kiatelluride.color)
    print(kiatelluride.year)




    landrover=Car("landrover","rover","grey", 2007)
    print(landrover.name)
    print(landrover.model)
    print(landrover.color)
    print(landrover.year)




    mercedes=Car("mercedes","benz","grey", 2009)
    print(mercedes.name)
    print(mercedes.model)
    print(mercedes.color)
    print(mercedes.year)