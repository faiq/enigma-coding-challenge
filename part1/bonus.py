import csv

from cleaning import write_to_file
from validate import DateValidator

def main():
    edited_rows = read_and_validate()
    write_to_file(edited_rows, 'bonus.csv')
            
def read_and_validate():
    edited_rows = list()
    validator = DateValidator()
    with open('test.csv', 'r+') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            date = row['start_date'] 
            is_valid = validator.is_normal_date(date)
            normalized = ''
            if not is_valid: 
                normalized = validator.normalize_date(date)
            if normalized is '':
                row['start_date_description'] =  date # filter all the bad dates here 
            else: 
                row['start_date_description'] =  '' # no bad dates here
            row['start_date'] = normalized
            edited_rows.append(row)
    return edited_rows


if __name__ == "__main__":
    main()
