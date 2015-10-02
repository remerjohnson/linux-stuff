# Work Scripts Explanation

'form2_script.py' is a Python script that will take an HTML file, specifically an HTML file that is an email sent by UCSD data providers filling out the 'Form 2' RDCP form, and insert the responses into appropriate columns in a .csv file. This was needed because the email was the only place the responses were going: there is no database or tabular data for this information.     

# Requirements

* Python 2.7.x  
* [BeautifulSoup 4.4](http://www.crummy.com/software/BeautifulSoup/bs4/download/) - [BeautifulSoup documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)  

# Usage 

* Right-click 'Save As...' on `form2_script.py` above to get the script.   
* Save the RDCP Form 2 email response in Outlook as `form2.html` (it _must_ be named this name) in _same_ directory as `form2_script.py` you downloaded the script to.   
* Open a terminal and `cd` to the directory that contains both `form2.html` and `form2_script.py`  
* Typing `python form2_script.py` in the terminal will produce the .csv file `form2_output.csv`. It will produce the questions in the columns, and insert the responses as a row in the spreadsheet.  
* (Optional) you can open the .csv in LibreOffice and export to Excel formats (.xls and .xlsx) if you need it to be in those formats.    

# Known Issues

* Since it relies on the csv library in Python, UTF-8 support for certain fields may not always work. I have tried to specify UTF-8 explicitly where possible, but some fields simply don't support it.  
* Very large description fields may have slight formatting issues, so manual review is necessary.  

# Acknowledgement

This particular script was used with great help from the resource: 

*Jeri Wieringa , "Intro to Beautiful Soup," Programming Historian (30 December 2012), http://programminghistorian.org/lessons/intro-to-beautiful-soup.html*
