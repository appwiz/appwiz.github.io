import sys
import re
import csv

def main(filename='files.csv'):
    links = []
    writing = []

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')

        for row in reader:
            check_file(row[0], links=links, writing=writing)

    print('<h3>writing</h3>')
    for x in writing:
        print(x)

def check_file(filename, links, writing):
    with open(filename, 'r') as f:
        contents = f.read()

        link_page_sentinel = r'(.*)<p><em>Original article is at(.*)'
        link_page_match = re.search(link_page_sentinel, contents)
        if link_page_match:
            links.append(filename)
        else:
            writing.append(filename)

# ls *.html | grep -v index > linkifier/files.csv   
# python3 linkifier/writing-or-link.py linkifier/files.csv
if __name__ == "__main__":
    main(sys.argv[1])
