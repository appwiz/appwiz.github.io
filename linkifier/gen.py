import random
import sys

# write title to file
def write_file(template, url, title, slug):
    filename = slug + '.html'
    content = 'Please follow <a href="%URL%">%TITLE%</a>'
    content = content.replace('%URL%', url)
    content = content.replace('%TITLE%', title)

    template = template.replace('%CONTENT%', content)
    template = template.replace('%TITLE%', title)

    with open(filename, 'w') as f:
        f.write(template)
        f.flush()

def read_csv(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def main(filename='input.csv'):
    print(filename)
    lines = read_csv(filename)
    template = read_file('link.template')

    o = []
    for line in lines:
        if line.startswith('#'):
            continue

        if line.strip() == '':
            continue

        (url, title, slug) = line.split(',')
        url = url.replace('"', '')
        title = title.replace('"', '')
        slug = slug.strip().lower().replace('"', '').replace('_', '-')

        o.append('<li><a href="%SLUG%.html">%TITLE%</a></li>'.replace('%SLUG%', slug).replace('%TITLE%', title))

        write_file(template, url, title, slug)

    random.shuffle(o)

    for x in o:
        print(x)

# python main method
if __name__ == "__main__":
    main(sys.argv[1])

