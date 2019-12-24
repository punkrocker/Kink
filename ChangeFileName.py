# 修改Kink原始文件名，添加系列
import os
import urllib
from urllib.request import urlopen
from dto.Shoot import Shoot

for filename in os.listdir('G:\\'):
    if not os.path.isdir(filename) and filename.endswith('.mp4'):
        content = filename.split('_')
        user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}
        url = "https://www.kink.com/shoot/" + content[0]
        req = urllib.request.Request(url, None, headers)
        all_the_text = urlopen(req).read()
        shoot = Shoot(all_the_text)
        print(shoot.channel_name)

