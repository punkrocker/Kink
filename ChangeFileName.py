# 修改Kink原始文件名，添加系列
import os
import urllib
from urllib.request import urlopen
import re
import datetime
from dto.Shoot import Shoot

path = 'K:\\转移'


# 对比官网命名规则
def convert_to_kink_standard():
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


def convert_to_local_standard():
    for filename in os.listdir(path):
        if not os.path.isdir(filename) and filename.endswith('.mp4'):
            try:
                pattern = re.compile('\w+')
                matcher = re.search(pattern, filename)
                series = matcher.group(0)
                pattern = re.compile('\(\d+\)')
                matcher = re.search(pattern, filename)
                video_no = matcher.group(0).replace('(', '').replace(')', '')
                part = filename.split('-')
                time_str = part[1].strip()
                dt = str(datetime.datetime.strptime(time_str, "%b %d, %Y"))
                video_date = dt[:dt.index(' ')]
                actors = part[2].strip()
                new_name = series + ' ' + video_date + ' ' + video_no + ' ' + actors
                os.rename(path + '\\' + filename, path + '\\' + new_name)
            except:
                print('==============>err:', filename)


convert_to_local_standard()
