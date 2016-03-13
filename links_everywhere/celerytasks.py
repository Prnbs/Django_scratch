from __future__ import absolute_import

from links_everywhere.celery import app
from nlp.soup_nlp import get_text_and_img_from_url
# from links_everywhere.views import save_url_metadata

@app.task
def get_url_metadata(url):
    print("*"*50)
    print ("Parsing page ", url)
    blurb, img = get_text_and_img_from_url(url)
    print(blurb)
    print(img)
    # save_url_metadata(url, blurb, img)
    print("*"*50)
    return blurb, img


def dummyadd(url):
    result =  get_url_metadata.delay(url)
    return result.get()

