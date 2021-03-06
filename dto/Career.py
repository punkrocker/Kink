from bs4 import BeautifulSoup


class Career:
    def __init__(self, text, is_model=True):
        self.name = ''
        self.desc = ''
        self.tags = ''
        self.is_model = is_model
        self.parse_html(text)

    def get_model_name(self, soup):
        model_name = soup.find('h1', {'class', 'page-title'})
        [s.extract() for s in model_name('span')]
        self.name = str(model_name.text).strip()

    def parse_html(self, all_the_text):
        soup = BeautifulSoup(all_the_text, 'html.parser')
        self.get_model_name(soup)
        self.desc = str(soup.find('span', id='expand-text').text).strip()
        if self.is_model:
            tags = str(soup.find('div', {'class', 'model-tags'}).text).strip()
            self.tags = tags.replace('tags:', '').replace('\n', '').strip()
