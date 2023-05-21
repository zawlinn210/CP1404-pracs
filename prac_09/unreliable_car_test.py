from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar Class."""
    car = UnreliableCar("Audi", 100, 70)
    print(f"{car.name} drove {car.drive(20)}km.")


main()