import argparse
from bs4 import BeautifulSoup
from url_loader import get_url_content


def get_page_num(url):
    soup = BeautifulSoup(get_url_content(url), 'html.parser')
    page_nums = str(soup.find('nav', {'class', 'paginated-nav'}).text).strip().split('\n')
    return page_nums[-2]


def download_shoot(shoot_url):
    soup = BeautifulSoup(get_url_content(shoot_url), 'html.parser')
    download_links = soup.findAll('ul', {'class', 'full-movie open'})
    print(download_links)


def download_channel_page(channel_page_url):
    soup = BeautifulSoup(get_url_content(channel_page_url), 'html.parser')
    shoots = soup.findAll('a', {'class', 'shoot-link'})
    for shoot_index in range(len(shoots), 0, -1):
        shoot = shoots[shoot_index - 1]
        download_shoot('https://www.kink.com' + shoot.attrs['href'])


def download_channel(chanenl_name):
    url = 'https://www.kink.com/search?type=shoots&channelIds=' + chanenl_name + '&sort=published'
    page_num = int(get_page_num(url))
    for page in range(page_num, 0, -1):
        channel_page_url = 'https://www.kink.com/search?type=shoots&channelIds=' + chanenl_name + '&sort=published&page=' + str(
            page)
        download_channel_page(channel_page_url)
        break


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Personal information')
    parser.add_argument('--channel', dest='channel', type=str, help='Name of the candidate')
    args = parser.parse_args()
    download_channel(args.channel)
