"""
对比单页区别
"""

from bs4 import BeautifulSoup
import os

video_path = "G:\\"

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}
content = open('./target_html/video_list_page.html', 'r', encoding='utf-8').read()
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

files = os.listdir(video_path)
video_files = []
for file in files:
    if file.endswith('.mp4'):
        video_files.append(file)

downloaded_video = []
for number in page_videos:
    for file in video_files:
        if number in file:
            downloaded_video.append(number)
            continue

x = set(page_videos) - set(downloaded_video)
print(x)
print(len(x))
