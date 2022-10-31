from urllib.request import urlopen
from urllib.error import HTTPError
import urllib

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
cookie = "_ga=GA1.2.1827726319.1636797460; _privy_83DCC55BDFCD05EB0CBCF79C=%7B%22uuid%22%3A%22d4693051-fdf1-4aa7-a887-fd92cd076c39%22%2C%22variations%22%3A%7B%7D%2C%22country_code%22%3A%22TW%22%2C%22region_code%22%3A%22TW_19%22%2C%22postal_code%22%3A%22%22%7D; __zlcmid=1Ajl2ayL00KRRFp; _gid=GA1.2.1008576944.1659854210; amp_54ec17=wV25ItGt1Q1zNecgj-shHK.MzQzODQ0OQ==..1ga1cok5d.1ga1dbdjs.156.39e.4ek; _gali=favoritesSlider-item2; _gat_UA-58559267-1=1"
headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight', 'Cookie': cookie}


def get_url_content(url):
    try:
        req = urllib.request.Request(url, None, headers)
        content = urlopen(req).read()
        return content
    except HTTPError as e:
        print(e)
