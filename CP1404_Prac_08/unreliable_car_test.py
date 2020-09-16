from CP1404_Prac_08.unreliable_car import UnreliableCar


class UnreliableCarTest(UnreliableCar):

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi_Test instance, based on parent class Taxi."""
        super().__init__(name, fuel, reliability)
        super().drive(40)


if __name__ == '__main__':
    test = UnreliableCarTest("Prius 1", 100, 1.23)
    print(test)
