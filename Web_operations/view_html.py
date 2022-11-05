# import module
import codecs
import os

def main(location, base, sep, check_test):
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

    <p>Taylor</p>

    </body>
    </html>

    """
    # Overwrite the data
    f.write(html_template)

    # close the file
    f.close()

    # viewing html files
    # below code creates a 
    # codecs.StreamReaderWriter object

    file = codecs.open(complete_location, 'r', "utf-8")

    print(file.read())

if __name__ == '__main__':
    printFileData = True
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
    main(home, strBase, strFolderSep, printFileData)