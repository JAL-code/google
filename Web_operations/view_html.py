# import module
import codecs
import os

# import the parser application from the official python documention
from html.parser import HTMLParser

# import browser access to the web
import webbrowser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

def create_test_html(location, base, sep, check_test):
    # to open/create a new html fle in the write mode
    # add error code to locate correct problem
    complete_location = f"{location}{sep}GFG.html"

    if printFileData: 
        print( f"HTML Path    :{complete_location}" )

    f = open(complete_location, 'w')

    # the html code which will go in the file GFG.html
    html_template = """
    <html>
    <head>
    <title>Anti-Hero</title>
    </head>
    <body>
    <h2>It's me, hi! </h2>

    <p>I'm the problem, it's me!</p>

    <p>Hhhiii</p>

    <p>  ... Taylor ... </p>

    </body>
    </html>

    """
    # Overwrite the data
    f.write(html_template)

    # close the file
    f.close()
    return complete_location

def open_with_codecs(saved_location, check_test):

    # viewing html files
    # below code creates a 
    # codecs.StreamReaderWriter object
    print("Testing open with codecs.")
    file = codecs.open(saved_location, 'r', "utf-8")

    print(file.read())

def open_with_parser(complete_location, check_test):

    print("Testing open with parser.")
    # The Problem is here:  How to parse the text file?
    parser = MyHTMLParser()
    text_file = open(complete_location)
    
    contents = text_file.read()
    if check_test:
        print(contents)
    parser.feed(contents)

if __name__ == '__main__':
    printFileData = False

    # Ios = mode for mac system
    # Linux = mode for linux based system (not tested yet)
    # Win = mode for windows 
    # Google = mode for chrome (not tested yet)
    # Fox   = mode for Foxfire (not tested yet)
    webmode = 'Win'
    remove = len('Web_operations')
    strPath = os.path.realpath(__file__)
    
    strDir = os.path.dirname(__file__)
    home = strDir[:len(strDir)-remove-1]
    strBase = os.path.basename(__file__) 
    strFolderSep = os.path.sep
    if printFileData: 
        print( f"Full Path    :{strPath}" )
        print( f"Dir name     :{strDir}" ) 
        print( f"Base Name    :{strBase}" )
        print( f"HTML Home    :{home}")    
        print( f"Alt Name     :{strFolderSep}")

    default_location = create_test_html(home, strBase, strFolderSep, printFileData)

    open_with_codecs(default_location, printFileData)

    open_with_parser(default_location, printFileData)

    test_website = r"https://docs.python.org/3/library/html.parser.html"

    # Convert code to try method
    if webmode == 'Ios':
        c = webbrowser.get('safari')
    
    if webmode == 'Win':
        c = webbrowser.get('windows-default')
        
    c.open(test_website)
    c.open_new_tab(test_website)