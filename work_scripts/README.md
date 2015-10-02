# Work Scripts Explanation

'form2_script.py' is a script that will take an HTML file that is an email sent by data providers filling out the 'Form 2' RDCP form, and insert the responses into appropriate columns in a .csv file  

# Requirements

* Python 2.7.x  
* [BeautifulSoup 4.4](http://www.crummy.com/software/BeautifulSoup/bs4/download/) - [Beautiful documentation](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)  

# Usage 

* Right-click 'Save As...' on `form2_script.py`  
* Save RDCP Form 2 email in Outlook as `form2.html` in same directory as `form2_script.py`  
* `cd` to the directory that contains both `form2.html` and `form2_script.py`  
* `python form2_script.py` will produce the .csv file `form2_output.csv`

# Acknowledgement
This particular script was used with great help from the resource: 

*Jeri Wieringa , "Intro to Beautiful Soup," Programming Historian (30 December 2012), http://programminghistorian.org/lessons/intro-to-beautiful-soup.html*
