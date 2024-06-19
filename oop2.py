class car:
    def __init__(self,model,colours,manufucterer,yop):
        self.model = model
        self.colours = colours
        self.manufucterer = manufucterer
        self.yop = yop


    def speed(self):
        print("The manufucterer of",self.model,"is",self.manufucterer)


car1 = car("M12","white","BMW","2023")
car2 = car("M3","Black","Ferrari","2020")
car3 = car("M2","Yellow","Mercedes","2019")
car4 = car("R12","Pink","Audi","2063")

car1.speed()
car2.speed()
car3.speed()
car4.speed()
