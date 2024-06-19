class device:
    def __init__(self,model,yom):
        self.model = model
        self.yom = yom

    def crush(self):
        print(self.model, "has crushed")

computer = device("Hp",1992)
computer.crush()
laptop =device("Dell",2015)
laptop.crush()
