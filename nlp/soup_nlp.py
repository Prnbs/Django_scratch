import re
from bs4 import BeautifulSoup, NavigableString
from urllib.request import urlopen
import nltk


def soupify(url):
    page = urlopen(url)
    soup = BeautifulSoup(page.read())
    # get the title
    title_tag = soup.html.head.title.string
    # print all contents in all paragraph
    all_para = soup.find_all('p')
    for para in all_para:
        try:
            line = " ".join(para.contents)
            line = re.sub('[n]','', line)
            if len(line) >= 10:
                print(line)
        except:
            pass

    # everything in a body
    # for i in soup.body:
    #     print(i)


def get_text_from_url(url):
    page = urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page, 'lxml')
    # get all the text in the p tags
    all_para = soup.find_all('p')
    all_text = []
    for para in all_para:
        for tag in para:
            line = extract_text_from_tag(tag)
            if line is not None:
                # remove the following special characters
                line = re.sub(r'[\n\t\r|\xa0]+', '', line)
                line = line.strip()
                if len(line) > 0:
                    all_text.append(line)
    return ' '.join(all_text)


def extract_text_from_tag(tag):
    if type(tag) is NavigableString:
        return str(tag)
    elif type(tag.contents) is list:
        if len(tag.contents) > 0:
            try:
                return " ".join(tag.contents)
            except:
                pass


if __name__ == '__main__':
    text_data = get_text_from_url('https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm')
    # text_data = get_text_from_url('http://prnbs.github.io/')
    print(text_data)
