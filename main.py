import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
from bs4.element import Comment


def tag_visible(element):
    if element.parent.name in [
        'style',
        'script',
        'head',
        'title',
        'meta',
            '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def crawl(link):
    # Open the url
    src = urlopen(link)
    # Parse it in beautifulsoup
    codebase = BeautifulSoup(src, 'html.parser')
    prettyCode = codebase.prettify()
    # Finding all text elements in the webpage
    texts = codebase.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    # Filtering text to clean all the text in the webpage
    text = u" ".join(t.strip() for t in visible_texts)
    # Fetching all the anchor tags
    listOfAnchor = codebase.findAll("a")
    urls = []
    urlText = []
    for i in listOfAnchor:
        # Get text of anchor tag
        a = i.getText()
        # Get URL of anchor tag
        b = i.get("href")
        # maintaining a list of the text of url's
        urlText.append(a)
        # maintaining a list of URL's
        urls.append(b)
    print("Timestamp: " + time.strftime("%m/%d/%Y, %H:%M:%S"))
    # Looping to print text of URL's and URL's
    for i in range(len(urlText)):
        print("URL text =>> " + urlText[i])
        print("\n\n")
        print("Link = > " + urls[i])
    input("Press enter to crawl...")
    # Printing pretty soup
    print("Source Code of the webpage => ")
    print(prettyCode)
    input("Press enter to parse...")
    # Printing visible text of the webpage
    print("Text of the webpage => ")
    print(text)
    # Printing metadata
    print("Metadata of the webpage => ")
    print(urls)

# Take a URL input
x = input(
    "Enter any url (PS, copy the url directly from the web browser for easy usage) : ")
# Call the crawler
crawl(x)
