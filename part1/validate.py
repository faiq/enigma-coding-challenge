import datetime

class DateValidator(object):
	def __init__(self, normalized_fmt='%Y-%m-%d'):
		self.normal_fmt = normalized_fmt
		self.months = ['January', 
					   'February',	
					   'March',
					   'April', 
					   'May',
					   'June',
					   'July',
					   'August',
					   'September',
					   'October',
					   'November',
					   'December'
					   ]


	def is_normal_date(self, date_text):
		is_valid = True
		try:
			datetime.datetime.strptime(date_text, self.normal_fmt)
			is_valid = True
		except ValueError:
			is_valid = False
		return is_valid


	def normalize_date(self, date_text):
		''' we have dates that come in these formats
			1. 01/94
			2. 02/22/2002
			3. October 1993
			4. April 10, 2003
			5. Complete nonsense
			for cases 1 and 4 we return a string with the valid date other wise blank string
		'''
		try:
			mdy_slashes = datetime.datetime.strptime(date_text, '%m/%d/%Y')
			if mdy_slashes is not None:
				iso = mdy_slashes.isoformat()
				return iso[:iso.find('T')]
		except Exception:
			month_array = [(month in date_text) for month in self.months]
			try:
				month = month_array.index(True) + 1
				comma = date_text.index(',')
			except Exception:
				return ''
			# parse out date and year
			year = date_text[comma+2:]
			date = date_text[date_text.find(' ')+1:comma]
			return ('%s-%d-%s' %  (year, month, date))
		else:
			return ''
