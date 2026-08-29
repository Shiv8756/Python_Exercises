class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def display(self):
        print("Make ",self.make,"Model ",self.model, "Year ",self.year)

car1=Car("Toyota","Camry",2016)
car1.display()
