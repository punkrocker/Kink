from bs4 import BeautifulSoup


def get_shoot_name(soup):
    model_name = soup.find('h1', {'class', 'shoot-title'})
    [s.extract() for s in model_name('span')]
    return str(model_name.text).strip()


def parse_html(all_the_text):
    soup = BeautifulSoup(all_the_text, 'html.parser')
    shoot_title = get_shoot_name(soup)
    # desc = str(soup.find('span', id='expand-text').text).strip()
    # tags = str(soup.find('div', {'class', 'model-tags'}).text).strip()
    # tags = tags.replace('tags:', '').replace('\n', '').strip()
    print(shoot_title)


if __name__ == '__main__':
    content = open('./target_html/video.html', 'r', encoding='utf-8').read()
    parse_html(content)