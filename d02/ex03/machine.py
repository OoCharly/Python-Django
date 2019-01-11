import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.counter = 0

    class EmptyCup(HotBeverage):
        Name = "empty cup"
        Price = 0.90

        def description(self):
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):

        def __init__(self):
            super(Exception, self).__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.counter = 0
        print("The machine has been repaired")

    def serve(self, order: HotBeverage):
        if self.counter == 10:
            raise self.BrokenMachineException
        else:
            self.counter += 1
            if random.randint(0,1) == 1:
                out = self.EmptyCup()
            else:
                out = order()
            return out


if __name__ == "__main__":
    c = CoffeeMachine()
    for i in range(1, 30):
        try:
            print(c.serve(Cappuccino).description())
            print(c.serve(Cappuccino).description())
            print(c.serve(Coffee).description())
            print(c.serve(Coffee).description())
            print(c.serve(Tea).description())
            print(c.serve(Chocolate).description())
            print(c.serve(Tea).description())
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            c.repair()

