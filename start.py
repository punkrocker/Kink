from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib
from channel_parse import ChannelParse

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}


def get_url_content(url):
    req = urllib.request.Request(url, None, headers)
    all_the_text = urlopen(req).read()
    return all_the_text


def get_channels():
    channel_url = 'https://www.kink.com/channels'
    ch_parse = ChannelParse()
    channels = ch_parse.parse_html(get_url_content(channel_url))
    ch_parse.save_to_db(channels)


get_channels()
