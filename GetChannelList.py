from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}


def parse_html(all_the_text, channel_name):
    soup = BeautifulSoup(all_the_text, "html.parser")
    channels = soup.findAll("div", {"class", "new-channel-tile"})
    for channel in channels:
        print(channel['data-title'])


if __name__ == '__main__':
    content = open('./target_html/channel.html', 'r', encoding='utf-8').read()
    parse_html(content, '')
