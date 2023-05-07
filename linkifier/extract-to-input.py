import sys
import re

def main(filename):
    with open(filename, 'r') as f:
        contents = f.read()

        url = None
        title = None
        slug = None

        # extract the title
        title_regex = r'<h1>(.*)</h1>'
        title_match = re.search(title_regex, contents)
        if title_match:
            title = title_match.group().replace('<h1>', '').replace('</h1>', '')
        else:
            title = 'NO_TITLE_FOUND'

        # extract the url
        paragaph_regex = r'<p>(.*)</p>'
        paragraph_match = re.search(paragaph_regex, contents)
        if paragraph_match:
            paragraph = paragraph_match.group()

            url_regex = r'<a href="(.*)">'
            url_match = re.search(url_regex, paragraph)
            if url_match:
                url = url_match.group().replace('<a href="', '').replace('">', '')
            else:
                url = 'NO_URL_FOUND'
        else:
            paragraph = 'NO_PARAGRAPH_FOUND'

        # extract the slug           
        slug = filename.replace('.html.original.html', '')

        # display as csv
        print('"%s","%s","%s"' % (url, title, slug))


if __name__ == "__main__":
    main(sys.argv[1])
