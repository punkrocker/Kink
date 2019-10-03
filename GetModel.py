from dto.Career import Career

if __name__ == '__main__':
    content = open('./target_html/model.html', 'r', encoding='utf-8').read()
    model = Career(content)
    print(model.name)
    print(model.desc)
    print(model.tags)
