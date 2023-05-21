import datetime
from bs4 import BeautifulSoup


class Shoot:
    def __init__(self, text):
        self.shoot_id = ''
        self.shoot_name = ''
        self.actor_names = []
        self.director_names = []
        self.categories = []
        self.description = ''
        self.shoot_date = datetime.date
        self.channel_name = ''
        self.download_link = []
        self.parse_html(text)

    def get_shoot_name(self, soup):
        model_name = soup.find('h1', {'class', 'shoot-title'})
        [s.extract() for s in model_name('span')]
        self.shoot_name = str(model_name.text).strip()

    def parse_html(self, all_the_text):
        soup = BeautifulSoup(all_the_text, 'html.parser')
        # self.get_shoot_name(soup)
        # self.get_base_info(soup)
        # self.get_performers(soup)
        # self.get_director(soup)
        # self.get_categories(soup)
        # self.description = str(soup.find('div', {'class', 'description'}).text).strip()
        # self.get_shoot_date(soup)
        self.get_download_link(soup)

    def get_download_link(self, soup):
        download_content = soup.find('ul', {'class', 'full-movie'})
        download_content = download_content.find_all('li')
        for li in download_content:
            self.download_link.append(li.find('a')['href'])

    def get_shoot_date(self, soup):
        date = soup.find('div', {'class', 'shoot-info'})
        date = date.find('div', {'class', 'columns'})
        date = date.find('div', {'class', 'column'})
        date = str(date.find('p').text).strip().replace('Date: ', '')
        time_format = datetime.datetime.strptime(date, '%B %d, %Y')
        self.shoot_date = datetime.datetime.strftime(time_format, '%Y-%m-%d')

    def get_categories(self, soup):
        tags = soup.find('p', {'class', 'category-tag-list'})
        tags = tags.findAll('a')
        for t in tags:
            self.categories.append(t.text)

    def get_director(self, soup):
        directors = soup.find('p', {'class', 'director'})
        directors = directors.findAll('a')
        for d in directors:
            self.director_names.append(d.text)

    def get_performers(self, soup):
        performers = soup.find('p', {'class', 'starring'})
        performers = performers.findAll('a')
        for p in performers:
            self.actor_names.append(p.text)

    def get_base_info(self, soup):
        shoot_base = soup.find('div', {'class', 'shoot-page'})
        self.shoot_id = shoot_base['data-shootid']
        self.channel_name = shoot_base['data-sitename']
