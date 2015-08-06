# Enigma Coding Challege

This repo is my proposed solutions at [Enigma] (http://enigma.io/) coding challenges for thier data engineering position.

There are two parts to this:

## Part 1. CSV manipulation:
	### Problems:
	1. String cleaning - The bio field contains text with arbitrary padding, spacing and line breaks. Normalize these values to a space-delimited string.
	2. Code swap - There is a supplementary CSV file for download here: state_abbreviations.csv. This "data dictionary" contains state abbreviations alongside state names. 
	   For the state field of the input CSV, replace each state abbreviation with its associated state name from the data dictionary.
	3. Date offset (bonus) - The start_date field contains data in a variety of formats. These may include e.g., "June 23, 1912" or "5/11/1930" (month, day, year). But not all values are valid dates. 	      Invalid dates may include e.g., "June 2018", "3/06" (incomplete dates) or even arbitrary natural language. Add a start_date_description field adjacent to the start_date column to filter invalid date values into. 
	   Normalize all valid date values in start_date to ISO 8601 (i.e., YYYY-MM-DD).
	
	### My proposed solutions 
	1. `cleaning.py` this file cleans the bio field in the csv file `test.csv` and produces output file `output.csv` 
	2. `swap.py` this file repaces abbreviations with the appropriate state names and produces output file `fixed_state.csv`
	3. `bonus.py` this file filters uses the custom validation class I wrote `validate.py` to validate and normalize date strings. It also filters bad balues into `start_date_description` to the output file `bonus.csv`

## Part 2. Scraping:
	### Problem: 
	1.  Write a script to scrape a [sample site] (http://data-interview.enigmalabs.org/companies/) and output its data in JSON 
	
	### Solution: 
	1. `scraper.py` scrapes the site using `Beautiful soup` and `requests`, and outputs its results to `solution.json`
