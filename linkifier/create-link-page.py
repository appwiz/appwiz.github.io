import random
import sys
import csv

def write_html_file(template, url, title, slug):
    filename = slug + '.html'
    template = template.replace('%URL%', url)
    template = template.replace('%TITLE%', title)
    
    write_file(template, filename)

def write_file(template, filename):
    with open(filename, 'w') as f:
        f.write(template)
        f.flush()

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

# for i in `ls *.html.original.html | grep -v index`; do python3 linkifier/extract-to-input.py $i >> linkifier/input.csv; done;
def main(filename='input.csv'):
    link_template = read_file('link.template')

    o = []

    rows = 0
    skipped_rows_comments = 0
    skipped_rows_empty = 0
    skipped_no_url = 0

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        
        for row in reader:
            rows += 1

            if row[0].strip() == '':
                skipped_rows_empty += 1
                continue

            if row[0].strip().startswith('#'):
                skipped_rows_comments += 1
                continue

            if row[0].strip() == 'NO_URL_FOUND':
                skipped_no_url += 1
                continue

            (url, title, slug) = row

            url = url.strip().lower().replace('"', "").strip()
            title = title.strip()
            slug = slug.strip().lower().replace('"', "").replace('_', '-').strip()

            o.append('<li><a href="%SLUG%.html">%TITLE%</a></li>'.replace('%SLUG%', slug).replace('%TITLE%', title))

            write_html_file(link_template, url, title, slug)

    random.shuffle(o)

    print('rows: %d' % rows)
    print('skipped_blank: %d' % skipped_rows_empty)
    print('skipped_comments: %d' % skipped_rows_comments)
    print('skipped_no_url: %d' % skipped_no_url)

    for x in o:
        print(x)

if __name__ == "__main__":
    main(sys.argv[1])

