# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import csv
import re

soup = BeautifulSoup (open('form2.html'), 'html.parser')

f = csv.writer(open('form2_output.csv', 'w'))
f.writerow(['Title', 'Names', 'Date', 'Date Type', 'Collection Description', 'Brief Description', 'Citation', 'Creative Commons Licensing'])

# Variable for the collection title
title = soup.find(string=re.compile(r'^Collection Title', flags=re.MULTILINE))
title =  title[19:]

# Variable for names
# Finds all names, then puts them into an empty list 
# Also prints in UTF-8 to handle special characters in names
u_names = soup.find_all(string=re.compile(r'\s Full Name', flags=re.MULTILINE | re.UNICODE)) 
names = []
for name in u_names:
	names.append( str(name[22:].encode('UTF-8')) )
	continue

# Variable for the date
date = soup.find(string=re.compile(r'^Dates', flags=re.MULTILINE))
date = date[29:]

# Variable for the date type
date_type = soup.find(string=re.compile(r'^Date T', flags=re.MULTILINE))
date_type = date_type[12:]

# Description header variables
# Not printed, but nice to have to get the responses on the next lines
full_header = soup.find(string=re.compile(r'^Full ', flags=re.MULTILINE))
brief_header = soup.find(string=re.compile(r'^Brief ', flags=re.MULTILINE))

# Variable for the full description
full_desc = []
full1 = full_header.find_next(string=True)
full2 = full1.find_next(string=True)
full3 = full2.find_next(string=True)

full_desc.append(full1)
full_desc.append(full2)
full_desc.append(full3)

# Variable for the brief description, which takes the header then grabs next string
brief = brief_header.find_next(string=True)

# Variable for citations  <-- improve /w break loop?
# citation_header = soup.find(string=re.compile(r'^If the ', flags=re.MULTILINE))
# citation = citation_header.find_next(string=True)

# Variable for Creative Commons Licensing decision
cc = soup.find(string=re.compile(r'^Creative ', flags=re.MULTILINE))
cc = cc[35:]

f.writerow([title, '|'.join(names), date, date_type, full_desc, brief.encode('UTF-8'), '', cc])
