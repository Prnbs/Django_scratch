import re
from bs4 import BeautifulSoup, NavigableString
from urllib.request import urlopen
import nltk
from nltk.corpus import stopwords
import operator
import sys

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


def get_top_five(text_data):
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    text = ''.join(text_data)
    sentences = sent_detector.tokenize(text.lower().strip())
    stopped_sent = []
    ngram = []
    pattern=re.compile("[^\w']")
    # remove stopwords
    for sentence in sentences:
        # print sentence
        # clear up punctuations
        # print(sentence)
        cleaned_sentence = str(pattern.sub(' ', sentence))
        # remove stopwords
        words = [word for word in cleaned_sentence.split() if word not in stopwords.words('english')]
        joint = ""
        # if nothing is left after removing stopwords don't append
        if len(words) > 0:
            joint = " ".join(words)
        # print (joint)
        stopped_sent.append(joint)
    # create Ngrams
    for sentence in stopped_sent:
        ngram += nltk.trigrams(sentence.split())
    flat_ngram_list = [item for sublist in ngram for item in sublist]
    fdist = nltk.FreqDist(flat_ngram_list)
    sorted_x = sorted(fdist.items(), key=operator.itemgetter(1), reverse=True)
    for k in sorted_x[:7]:
        print ("".join(k[0]) + ":" + str(k[1]))


if __name__ == '__main__':
    # text_data = get_text_from_url('https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm')
    # print(sys.argv[1])
    text_data = get_text_from_url('http://ssarangi.github.io/Luajit-For-Python/')
    print(text_data)
    ngram = get_top_five(text_data)
    # print(text_data)
