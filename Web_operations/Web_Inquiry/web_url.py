# From Real Python: https://realpython.com/python-web-scraping-practical-introduction/
# All actions will be limited to human scrolling one page at a time.

# open an url in a program
from urllib.request import urlopen

# create the url
url = "http://olympus.realpython.org/profiles/aphrodite"
# open the page
page = urlopen(url)
# page is  HTTPResponse object
page
# decode the page using UTF-8
html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print the HTML
print(html)

# Get the html title
title_index = html.find("<title>")
print(f"title index is {title_index}")
start_index = title_index + len("<title>")
print(f"start position of title text is {start_index}")
end_index = html.find("</title>")
print(f"title end index is {end_index}")
title = html[start_index:end_index]
print(f"HTML title is {title}")