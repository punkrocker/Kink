from bs4 import BeautifulSoup


def parse_html(all_the_text):
    soup = BeautifulSoup(all_the_text, "html.parser")
    model_name = soup.find("h1", {"class", "page-title"})
    [s.extract() for s in model_name('span')]
    print(str(model_name.text).strip())


if __name__ == '__main__':
    content = open('./target_html/model.html', 'r', encoding='utf-8').read()
    parse_html(content)
