import re

def romanChecker(code):
	pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
	return re.search(pattern, code)
	
number = romanChecker(raw_input("\nPlease enter a roman number. I will tell you if it is valid or not. >> "))
if str(number)[:3] == "<_s":
	print "\nThis is a valid roman number!"
else:
	print "\nThis wasn't a valid roman number."
	
raw_input("\nPress any key to exit.")