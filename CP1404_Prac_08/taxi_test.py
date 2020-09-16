from CP1404_Prac_08.taxi import Taxi


class TaxiTest(Taxi):

    def __init__(self, name, fuel, price_per_km):
        """Initialise a Taxi_Test instance, based on parent class Taxi."""
        super().__init__(name, fuel, price_per_km)
        super().drive(100)


if __name__ == '__main__':
    test = TaxiTest("Prius 1", 100, 1.23)
    print(test)
