import csv

from cleaning import write_to_file
from validate import DateValidator

def main():
	read_and_validate()


			


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
				print normalized, date
	return edited_rows


if __name__ == "__main__":
	main()
