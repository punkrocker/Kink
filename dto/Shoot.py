import datetime


class Shoot:
    def __init__(self, soup):
        self.shoot_id = ''
        self.shoot_name = ''
        self.actor_names = []
        self.director_name = ''
        self.categories = []
        self.description = ''
        self.shoot_date = datetime.date
        self.channel_name = ''
        self.download_link = ''

    def get_shoot_name(self, soup):
        model_name = soup.find('h1', {'class', 'shoot-title'})
        [s.extract() for s in model_name('span')]
        self.shoot_name = str(model_name.text).strip()
