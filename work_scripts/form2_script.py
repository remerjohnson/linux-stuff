from bs4 import BeautifulSoup
import csv
import re

soup = BeautifulSoup (open('form2.html'), 'html.parser')

f = csv.writer(open('bs_output.csv', 'w'))
f.writerow(['Title', 'Names', 'Date', 'Date Type', 'Collection Description', 'Brief Description', 'Citation', 'Creative Commons Licensing'])

# Variable for the collection title
title = soup.find(string=re.compile(r'^Collection Title', flags=re.MULTILINE))
title =  title[19:]

# Variable for names (Note: because of nastiness earlier in the HTML, 
# prints a nasty big line in the beginning. Also, can't force UTF-8 encoding on a list
u_names = soup.find_all(string=re.compile(r'\s Full Name', flags=re.MULTILINE | re.UNICODE)) 
names = []
for name in u_names:
	names.append( str(name[22:]) )
	continue

# Variable for the date
date = soup.find(string=re.compile(r'^Dates', flags=re.MULTILINE))
date = date[29:]

# Variable for the date type
date_type = soup.find(string=re.compile(r'^Date T', flags=re.MULTILINE))
date_type = date_type[12:]

# Variable for the brief description, which takes the header then grabs next string
brief_header = soup.find(string=re.compile(r'^Brief ', flags=re.MULTILINE))
brief = brief_header.find_next(string=True)

# Variable for citations  <-- improve /w break loop?
# citation_header = soup.find(string=re.compile(r'^If the ', flags=re.MULTILINE))
# citation = citation_header.find_next(string=True)

# Variable for Creative Commons Licensing decision
cc = soup.find(string=re.compile(r'^Creative ', flags=re.MULTILINE))
cc = cc[35:]

f.writerow([title, names, date, date_type, '', brief.encode('UTF-8'), '', cc])
