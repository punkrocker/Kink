"""
对比单页区别
"""

from bs4 import BeautifulSoup
import os

page = 25
video_path = ["G:\\SAS\\" + str(page)]


def get_diff(paths):
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
    video_files = []
    for path in paths:
        files = os.listdir(path)
        for file in files:
            if file.endswith('.mp4'):
                video_files.append(file)
    downloaded_video = []
    for number in page_videos:
        for file in video_files:
            if number in file:
                downloaded_video.append(number)
                continue
    return page_videos, downloaded_video


page_videos, downloaded_videos = get_diff(video_path)

not_in_path = set(page_videos) - set(downloaded_videos)
for a in not_in_path:
    print(a)
print(len(not_in_path))

# print('=========================================')
# # downloaded_path = 'P:\\Tuf\\转移tUF'
# downloaded_path = 'Q:\\转移'
# files = os.listdir(downloaded_path)
# for file in files:
#     for num in not_in_path:
#         if (num in file):
#             print(file)
