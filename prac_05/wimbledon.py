"""
Game, Set, Match
Estimate: 35 minutes
Actual:   38 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_NAME_INDEX = 2


def main():
    """Read and display data about Wimbledon gentlemen's singles champions."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_data(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Read the records."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def process_data(records):
    """Process the data."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_NAME_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_NAME_INDEX]] = 1
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and countries."""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
