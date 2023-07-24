# From Real Python: https://realpython.com/python-web-scraping-practical-introduction/
# All actions will be limited to human scrolling one page at a time.

# open an url in a program
from urllib.request import urlopen

# create the url
url = "http://olympus.realpython.org/profiles/poseidon"
# open the page
page = urlopen(url)
# decode the page using UTF-8
html = page.read().decode("utf-8")
# print the HTML
print(html)

# Get the html title
start_index = html.find("<title >") + len("<title >")

end_index = html.find("</title>")

title = html[start_index:end_index]
print(f"HTML title is {title}")