from bs4 import BeautifulSoup


def get_model_name(soup):
    model_name = soup.find('h1', {'class', 'page-title'})
    [s.extract() for s in model_name('span')]
    return str(model_name.text).strip()


def parse_html(all_the_text):
    soup = BeautifulSoup(all_the_text, 'html.parser')
    model_name = get_model_name(soup)
    desc = str(soup.find('span', id='expand-text').text).strip()
    print(model_name, desc)


if __name__ == '__main__':
    content = open('./target_html/director.html', 'r', encoding='utf-8').read()
    parse_html(content)