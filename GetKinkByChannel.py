from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib
import pymysql
import Config
import sys


def get_channel(channel_name, end_page):
    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}
    for page in range(1, int(end_page) + 1):
        url = "https://www.kink.com/channel/" + channel_name + "/latest/page/" + str(page)
        get_url_content(headers, url, channel_name)


def get_url_content(headers, url, channel_name):
    try:
        req = urllib.request.Request(url, None, headers)
        all_the_text = urlopen(req).read()
    except HTTPError as e:
        print(e)
    else:
        soup = BeautifulSoup(all_the_text, "html.parser")
        result = soup.find("div", {"class", "shoot-list"})
        shoots = result.findAll("div", {"class", "shoot"})
        for child in shoots:
            try:
                performer = child.find("div", {"class", "shoot-thumb-models"}).get_text().strip()
                video_name = child.find("div", {"class", "script"}).get_text().strip()
                video_no = child.a.get("href").replace("/shoot/", "")
                pic = child.find("img", {"class", "adimage"}).get("src")
                if (not pic.startswith("http")):
                    continue
                try:
                    conn = pymysql.connect(host=Config.HostIP, user=Config.UserName, passwd=Config.Password,
                                           db=Config.DBName, port=Config.Port, charset=Config.Charset)
                    cur = conn.cursor()
                    sql = "select count(1) as num from t_videos where videono = '" + video_no + "'"
                    cur.execute(sql)
                    r = cur.fetchall()
                    if (r[0][0] > 0):
                        continue;
                    else:
                        # 下载图片
                        try:
                            path = Config.Path
                            pic_location = path + video_no + ".jpg"
                            picconn = urllib.request.urlopen(pic)
                            f = open(pic_location, 'wb')
                            f.write(picconn.read())
                            f.close()
                        except HTTPError as e:
                            print(e)
                    sql = "insert into t_videos (companyname,videono,status,performer,img,videoname,channel) values ('Kink','" + video_no.replace(
                        '\'', '\\\'') + "','0','" + performer.replace('\'',
                                                                      '\\\'') + "','" + video_no + ".jpg" + "',' " + video_name.replace(
                        '\'', '\\\'') + " ','" + channel_name + "')"
                    cur.execute(sql)
                    conn.commit()
                    print(video_no + ":SUCCESS")
                except Exception as ex:
                    print(ex)
                finally:
                    cur.close()
                    conn.close()
            except  Exception as e:
                print(e)


sys.argv[0] = "theupperfloor"
user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}
url = "https://www.kink.com/channel/" + sys.argv[1] + "/latest/page/1"
try:
    req = urllib.request.Request(url, None, headers)
    all_the_text = urlopen(req).read()
except HTTPError as e:
    print(e)
else:
    soup = BeautifulSoup(all_the_text, "html.parser")
    result = soup.find("div", {"class", "shoot-list"})
    shoots = result.findAll("a", {"class", "page-normal"})
    last = shoots[-1].get_text().strip()
    get_channel(sys.argv[1], last)
print("finish")
