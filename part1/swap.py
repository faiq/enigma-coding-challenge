import csv
from cleaning import write_to_file


def main():
    abbreviations = get_abbreviations()
    edited_rows = read_and_replace(abbreviations)
    write_to_file(edited_rows, 'fixed_state.csv')


def get_abbreviations():
    # Return a dict of state_name: abbreviation for O(1) access
    abbreviations = {}
    with open('state_abbreviations.csv', 'r+') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i > 0:
                # skip the headers
                abbreviations[row[0]] = row[1]
    return abbreviations


def read_and_replace(abbreviations):
    edited_rows = list()
    with open('test.csv', 'r+') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            state = row['state']
            row['state'] = abbreviations[state]
            edited_rows.append(row)
    return edited_rows


if __name__ == "__main__":
    main()
