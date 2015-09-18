# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import csv
import re

# make the soup object as per instructions in Beautiful Soup 4, open the file and use HTML parser
soup = BeautifulSoup (open('form2.html'), 'html.parser')

# write all our header rows
f = csv.writer(open('form2_output.csv', 'w'))
f.writerow(['Title', 'Names', 'Date', 'Date Type', 'Keywords/Topics', 'Collection Description', 
	'Brief Description', 'Existing identifiers?', 'DOIs for each object?', 'Creative Commons Licensing'])

# variable to find the collection title
title = soup.find(string=re.compile(r'^Collection Title', flags=re.MULTILINE))
# slice only the characters we need
title =  title[20:]

# Variable to find names
# Finds all names, then puts them into an empty list sliced 
# Also prints in UTF-8 to handle special characters in names
# as csv package doesn't handle UTF-8
u_names = soup.find_all(string=re.compile(r'\s Full Name', flags=re.MULTILINE | re.UNICODE)) 
names = []
for name in u_names:
	names.append( str(name[23:].encode('UTF-8')) )
	continue

# Variable to find the date
date = soup.find(string=re.compile(r'^Dates', flags=re.MULTILINE))
# slice only the characters we need
date = date[30:]

# Variable to find the date type
date_type = soup.find(string=re.compile(r'^Date T', flags=re.MULTILINE))
# slice only the characters we need
date_type = date_type[13:]

# Variable for keywords/topics
keywords = soup.find(string=re.compile(r'^Keywords', flags=re.MULTILINE))
# slice only the characters we need
keywords = keywords[19:] 

# Set up Description sections header variables
# Nice to have to get the responses on the next or previous lines
full_header = soup.find(string=re.compile(r'^Full ', flags=re.MULTILINE))
brief_header = soup.find(string=re.compile(r'^Brief ', flags=re.MULTILINE))
brief_header_prev = brief_header.find_previous(string=True)

# Create empty list for the full description
full_desc = []
# Create a variable to find ALL strings after full_header
full1 = full_header.find_all_next(string=True)
# Create a variable to find ALL strings after brief_header
# The idea is this will isolate all unneeded lines after the full description
brief1 = brief_header_prev.find_all_next(string=True)

# Append the empty full_desc list with ALL lines after header
for lines in full1:
	lines = lines.lstrip()
	full_desc.append( str(lines.encode('UTF-8')) )

# Remove all unneeded lines from the full_desc list we just populated
for lines in brief1:
	lines = lines.lstrip()
	full_desc.remove( str(lines.encode('UTF-8')) )

# badlines = full_desc.find_all(string=re.compile(r'^\W'))

#for line in full_desc:
#	if line.startswith(' '):
#		re.sub(r'^ ','', lines, flags=re.MULTILINE | re.UNICODE)

# Variable to find the brief description, which takes the header then grabs next string
brief = brief_header.find_next(string=True)

# Variable to find response to the question of if they already have identifiers for the data
exist_id = soup.find(string=re.compile(r'^Do you al', flags=re.MULTILINE))
exist_id = exist_id[50:]

#
doi_request = soup.find(string=re.compile(r'^Do you wa', flags=re.MULTILINE))
doi_request = doi_request[60:]

# Variable for citations  <-- improve /w break loop?
# citation_header = soup.find(string=re.compile(r'^If the ', flags=re.MULTILINE))
# citation = citation_header.find_next(string=True)

# Variable for Creative Commons Licensing decision
cc = soup.find(string=re.compile(r'^Creative ', flags=re.MULTILINE))
cc = cc[35:]

f.writerow([title, '| '.join(names), date, date_type, keywords.replace(',', ' |'), '\n'.join(full_desc), 
	brief.encode('UTF-8'), exist_id, doi_request, cc])
