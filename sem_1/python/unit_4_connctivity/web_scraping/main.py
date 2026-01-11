from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://tatamumbaimarathon.procam.in/results/race-results"

'''
url = "https://tatamumbaimarathon.procam.in/results/race-results"
This is the address of the webpage
It contains the dataset you want to scrape
Think of it as a home address

📌 Interview line:
The URL specifies the location of the web resource from which data is to be retrieved.
'''


html = urlopen(url)

print(type(html))

soup = BeautifulSoup(html, "lxml")
print(type(soup))

# title of the page
title = soup.title
print(title)


text = soup.get_text()
print(text)
'''
Why?

To verify you loaded the correct page
To see raw content without tags
'''


