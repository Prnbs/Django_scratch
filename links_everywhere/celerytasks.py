from __future__ import absolute_import

from links_everywhere.celery import app
from bs4 import BeautifulSoup
from urllib.request import urlopen

@app.task
def get_url_metadata(url):
    print ("Calling add")
    page = urlopen(url)
    soup = BeautifulSoup(page.read())
    # first read the meta tag
    print(soup)
    return True


def dummyadd(url):
    return get_url_metadata.delay(url)
