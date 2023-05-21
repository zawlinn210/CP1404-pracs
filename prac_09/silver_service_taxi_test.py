from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi class."""
    taxi = SilverServiceTaxi("Toyota", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()