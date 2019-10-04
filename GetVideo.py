from bs4 import BeautifulSoup


def get_shoot_name(soup):
    model_name = soup.find('h1', {'class', 'shoot-title'})
    [s.extract() for s in model_name('span')]
    return str(model_name.text).strip()


def parse_html(all_the_text):
    soup = BeautifulSoup(all_the_text, 'html.parser')
    shoot_title = get_shoot_name(soup)
    shoot_base = soup.find('div', {'class', 'shoot-page'})
    shoot_id = shoot_base['data-shootid']
    shoot_channel = shoot_base['data-sitename']
    performers = soup.find('p', {'class', 'starring'})
    performers = performers.findAll('a')
    # for p in performers:
    #     print(p.text)
    # directors = soup.find('p', {'class', 'director'})
    # directors = directors.findAll('a')
    # for d in directors:
    #     print(d.text)
    # tags = soup.find('p', {'class', 'category-tag-list'})
    # tags = tags.findAll('a')
    # for t in tags:
    #     print(t.text)
    desc = str(soup.find('div', {'class', 'description'}).text).strip()
    date = soup.find('div', {'class', 'shoot-info'})
    date = date.find('div', {'class', 'columns'})
    date = date.find('div', {'class', 'column'})
    date = str(date.find('p').text).strip().replace('Date: ', '')
    print(date)


if __name__ == '__main__':
    content = open('./target_html/video.html', 'r', encoding='utf-8').read()
    parse_html(content)
