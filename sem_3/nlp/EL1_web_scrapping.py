'''web scraping is the process of extracting data 
from the websites instead of copying.
It includes:'''
#1) fetching web pages 
# requesting the webpage content using tools/libraries

#2) parsing their content 
# Example: If you get this raw HTML:
'''
<div>
  <h2>Product Name</h2>
  <span class = "Price">$120</span>
</div>
'''
#before parsing:
'''its just a text with tags
'''

#after parsing:
'''Heading -> "Product Name"
price -> "$120"
in python libraries like BeautifulSoup , lxml, 
or scrapy are used for parsing
'''

#3) extracting specific information
'''Take out the data which u need
'''


# code
import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

# Send GET request
response = requests.get(url)

print("Status Code:", response.status_code)

# Convert HTML into BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)
print(soup.title.get_text)


# # Find all quote elements
# quotes = soup.find_all("span", class_="text")

# # Print quotes
# for quote in quotes:
#     print(quote.text)

# 
quotes = soup.find_all("div", class_="quote")
print("Number of quots: ",len(quotes))

# for quote in quotes:
#     print(quote)
#     print("_"*50)

# get al the authors name
authors=soup.find_all("small",class_="author")
for author in authors:
    print(author.get_text())


# ------------------------Exercise: Scrape the Latest News Section from The Hindu

# 1) Import the required libraries: requests and BeautifulSoup
import requests
from bs4 import BeautifulSoup


# 2) Send a GET request to "https://www.thehindu.com/"
#    and print the status code of the response
url = "https://www.thehindu.com/"

response = requests.get(url)

print("Status Code:", response.status_code)


# 3) Print the raw HTML content of the page
print(response.text)


# 4) Parse the HTML content using BeautifulSoup
#    with the "lxml" parser and print the <title> tag
soup = BeautifulSoup(response.text, "lxml")

print(soup.title)


# 5) Print only the title text of the page
print(soup.title.text)


# 6) Use find_all() to extract all <ul> tags with class "timeline" (latest news section)
ul_tags = soup.find_all("ul", class_="timeline")
print(ul_tags)


# 7) Extract all news headline items from the timeline section
#    and store them in a list called trending_news

trending_news = []

# Find all timeline/news items
news_items = soup.find_all("li")

for item in news_items:
    text = item.get_text(" ", strip=True)

    if text:
        trending_news.append(text)


# 8) Print the list trending_news containing the raw news text

print("Trending News:")
print(trending_news)


# 9) Split each news item into timestamp and headline
#    and store them in two separate lists

timestamp = []
latestnews = []

for news in trending_news:

    # Split the news item into words
    parts = news.split(" ", 1)

    # If there are at least two parts
    if len(parts) == 2:
        time = parts[0]
        headline = parts[1]

        timestamp.append(time)
        latestnews.append(headline)


# 10) Print the timestamp list and latestnews list

print("Timestamp:")
print(timestamp)

print("\nLatest News:")
print(latestnews)