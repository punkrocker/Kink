from Career import Career

if __name__ == '__main__':
    content = open('./target_html/director.html', 'r', encoding='utf-8').read()
    director = Career(content, is_model=False)
    print(director.name)
    print(director.desc)
