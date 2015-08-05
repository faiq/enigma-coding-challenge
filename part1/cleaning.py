import csv


def main():
	edited_rows = read_and_clear()
	write_to_file(edited_rows, 'edited.csv')


def read_and_clear():
	edited_rows = list()
	with open('test.csv', 'r+') as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			bio = row['bio']
			clean_bio = clean_string(bio)
			row['bio'] = clean_bio
			edited_rows.append(row)
	return edited_rows


def write_to_file(json_list=None, file_name='output.csv'):
	with open(file_name, 'w') as out_file:
		try:
			# putting this in a try catch because json_list might not be a list or
			# could be None. This is likely to throw an attribute error
			field_names = json_list[0].keys()
			writer = csv.DictWriter(out_file, fieldnames=field_names)
			writer.writeheader()
			for row in json_list:
				writer.writerow(row)
		except AttributeError:
			print 'there was a problem getting the keys from the object'


def clean_string(string):
	string = string.replace('\n', '')
	string = string.replace('\t', '')
	sentences = string.split('.')
	for i, sentence in enumerate(sentences):
		clean = sentence.strip()
		sentences[i] = clean
	return '.'.join(sentences)


if __name__ == "__main__":
	main()
