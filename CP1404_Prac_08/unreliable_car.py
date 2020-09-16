from CP1404_Prac_08.taxi import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        self.reliability = random.uniform(0, 100)
        if self.reliability > distance:
            distance -= self.reliability
            self.odometer += self.reliability

        else:
            distance = self.reliability
            self.reliability = 0

        return distance




#if __name__ == '__main__':
    #test = TaxiTest("Prius 1", 100, 1.23)
    #print(test)
