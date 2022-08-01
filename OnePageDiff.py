"""
对比单页区别
"""

from bs4 import BeautifulSoup
import os
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib

page = 3
# video_path = ["N:\\SAS1-17\\" + str(page)]
# video_path = ["G:\\SAS\\" + str(page)]
video_path = ["N:\KinkUniversity\\" + str(page),
              "N:\\转移",
              "G:\\SAS\\KU",
              "N:\KinkUniversity"
              ]
url = "https://www.kink.com/channel/kinkuniversity/latest/page/" + str(page)
downloaded_full_path = []


def get_diff(paths):
    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}
    content = open('./target_html/video_list_page.html', 'r', encoding='utf-8').read()
    try:
        req = urllib.request.Request(url, None, headers)
        content = urlopen(req).read()
    except HTTPError as e:
        print(e)
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find("div", {"class", "shoot-list"})
    shoots = result.findAll("div", {"class", "shoot"})
    page_videos = []
    for child in shoots:
        try:
            video_no = child.a.get("href").replace("/shoot/", "")
            page_videos.append(video_no)
        except Exception as e:
            print(e)
    video_files = []
    for path in paths:
        files = os.listdir(path)
        for file in files:
            if file.endswith('.mp4'):
                video_files.append(path + file)
    downloaded_video = []
    for number in page_videos:
        for file in video_files:
            if number in file:
                downloaded_video.append(number)
                downloaded_full_path.append(path + file)
                continue
    return page_videos, downloaded_video


page_videos, downloaded_videos = get_diff(video_path)

not_in_path = set(page_videos) - set(downloaded_videos)
list.sort(downloaded_full_path)
for a in not_in_path:
    print(a)
print(len(not_in_path))
print("===================")
for file in downloaded_full_path:
    print(file)
