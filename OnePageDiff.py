"""
对比单页区别
"""

from bs4 import BeautifulSoup
import sys

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
print(page_videos)
