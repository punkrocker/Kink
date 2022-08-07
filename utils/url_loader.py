from urllib.request import urlopen
from urllib.error import HTTPError
import urllib

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}


def get_url_content(url):
    try:
        req = urllib.request.Request(url, None, headers)
        content = urlopen(req).read()
        return content
    except HTTPError as e:
        print(e)
