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
        self.download_link = ''
        self.parse_html(text)

    def get_shoot_name(self, soup):
        model_name = soup.find('h1', {'class', 'shoot-title'})
        [s.extract() for s in model_name('span')]
        self.shoot_name = str(model_name.text).strip()

    def parse_html(self, all_the_text):
        soup = BeautifulSoup(all_the_text, 'html.parser')
        self.get_shoot_name(soup)
        shoot_base = soup.find('div', {'class', 'shoot-page'})
        self.shoot_id = shoot_base['data-shootid']
        self.channel_name = shoot_base['data-sitename']
        performers = soup.find('p', {'class', 'starring'})
        performers = performers.findAll('a')
        for p in performers:
            self.actor_names.append(p.text)
        directors = soup.find('p', {'class', 'director'})
        directors = directors.findAll('a')
        for d in directors:
            self.director_names.append(d.text)
        tags = soup.find('p', {'class', 'category-tag-list'})
        tags = tags.findAll('a')
        for t in tags:
            self.categories.append(t.text)
        self.description = str(soup.find('div', {'class', 'description'}).text).strip()
        date = soup.find('div', {'class', 'shoot-info'})
        date = date.find('div', {'class', 'columns'})
        date = date.find('div', {'class', 'column'})
        date = str(date.find('p').text).strip().replace('Date: ', '')
        time_format = datetime.datetime.strptime(date, '%B %d, %Y')
        self.shoot_date = datetime.datetime.strftime(time_format, '%Y-%m-%d')
        download_content = soup.find('div', {'class', 'member-content'})
        download_content = download_content.find('div', {'class', 'full'})
        self.download_link = download_content.find('li').find('a')['href']
