import re
from bs4 import BeautifulSoup, NavigableString
from urllib.request import urlopen
import nltk
from nltk.corpus import stopwords
import operator


def get_text_and_img_from_url(url):
    page = urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page, 'lxml')
    # TODO call these two in parallel
    img = get_img_url(soup)
    blurb = get_text(soup)
    return blurb, img


def get_text(soup):
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


def get_img_url(soup):
    '''
    Just gets the first image in the page
    :param soup:
    :return:
    '''
    first_image = soup.find_all('img')[0]
    return first_image['src']


def extract_text_from_tag(tag):
    min_words = 5
    if type(tag) is NavigableString:
        str_between_tags = str(tag)
        # return only if more than min_words
        if len(str_between_tags.split()) > min_words:
            return str(tag)
    elif type(tag.contents) is list:
        # return only if more than min_words
        if len(tag.contents) > min_words:
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
    text_data = get_text_and_img_from_url('http://rhodesmill.org/brandon/')
    # print(text_data)
    ngram = get_top_five(text_data)
    # print(text_data)
