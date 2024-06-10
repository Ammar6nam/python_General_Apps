class employee:
    def __init__(self,name,salary=0) -> None:
        self. name=name
        self.salary=salary

    def giveRaise(self,percent):
        self.salary+=self.salary+



class chef(employee):

    def __init__(self, name) -> None:
        super().__init__(name, 50000)

    def work(self):
        print(self.name + 'Interfaces with customers')

class server(employee):
    def __init__(self, name) -> None:
        super().__init__(self, name)

    def work (self):
        print(self.name + 'Interfaces with customers')

class foodRobot(chef):
    def __init__(self, name) -> None:
        chef.__init__(name,name)

    def work(self):
        print(self.name + 'Interfaces with customers')

class customer:
    def __init__(self,name) -> None:
        self.name=name
    def order (self.name)


