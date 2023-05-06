from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'


def main():
    guitars = []
    in_file = open(FILENAME, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    for guitar in guitars:
        guitars.sort()
        print(guitar)

    name = input("Enter guitar name: ")
    year = int(input("Enter year: "))
    price = float(input("Enter price: "))
    write_to_file(name, price, year)


def write_to_file(name, price, year):
    with open(FILENAME, 'a') as out_file:
        print(f"{name},{year},{price:.2f}", file=out_file)


main()
