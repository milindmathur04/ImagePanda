# Import modules for CGI handling 
import cgi, cgitb,requests, re
from bs4 import BeautifulSoup

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
formInput = form.getvalue('val')

def test(form):
    r = requests.get(form)

    soup = BeautifulSoup(r.content)

    date = soup.find_all("table", {"class": "infobox"})

    for item in date:
        dates = item.find_all("th")
        for item2 in dates:
            if item2.text == "Original run":
                test2 = item2.find_next("td").text.encode("utf-8")
                mysub = re.sub(r'\([^)]*\)', '', test2)
                return mysub

test(formInput)