from dto.Shoot import Shoot

if __name__ == '__main__':
    content = open('./target_html/video.html', 'r', encoding='utf-8').read()
    shoot = Shoot(content)
    print(shoot.shoot_id)
    print(shoot.shoot_name)
    print(shoot.channel_name)
    print(shoot.actor_names)
    print(shoot.director_names)
    print(shoot.categories)
    print(shoot.description)
    print(shoot.download_link)
