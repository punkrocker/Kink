from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib
import re
import pymysql
import Config

def getMagnet(num):
    try:
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = { 'User-Agent' : user_agent }
        url = "https://thepiratebay.org/search/" + num + "/0/99/500"
        req = urllib.request.Request(url,None,headers)
        all_the_text = urlopen(req).read()
    except HTTPError as e:
        print(e)
    else:
        soup = BeautifulSoup(all_the_text, "html.parser")
        result = soup.find(id="searchResult")
        head = result.thead
        n = 0
        selectVideoName = ""
        selectVideoLink = ""
        maxSize = 0
        for child in head.next_siblings:
            try:
                n += 1
                if (n%2 == 0):
                    videoName = child.find("a", {"class": "detLink"})
                    videoLink = child.find("a", {"href": re.compile("magnet:?[^\"]+")})
                    if selectVideoName == "":
                        selectVideoName = videoName.get_text()
                    if selectVideoLink == "":
                        selectVideoLink = videoLink.get("href")
                    desc = child.find("font", {"class", "detDesc"}).get_text().split(',')
                    uploader = desc[2].strip().split(' ')[2].strip()
                    # 判断上传者,如果不是merzedes,就继续检测下一条
                    if uploader != 'merzedes':
                        continue
                    sizeDesc = desc[1].strip().split(' ')[1]
                    sizeNum = float(sizeDesc.split('\xa0')[0])
                    sizeUnit = sizeDesc.split('\xa0')[1]
                    if sizeUnit == 'GiB':
                        sizeNum *= 1024
                    if sizeNum > maxSize:
                        maxSize = sizeNum
                        selectVideoLink = videoLink.get("href")
                        selectVideoName = videoName.get_text()
            except Exception as e:
                print(e)
        try:
            conn=pymysql.connect(host=Config.HostIP,user=Config.UserName,passwd=Config.Password,db=Config.DBName,port=Config.Port,charset=Config.Charset)
            cur=conn.cursor()
            sql = "update t_videos set status = 1,piratename = '" + selectVideoName + "', magnetlink = '" + selectVideoLink + "',size = '" + str(maxSize) + "',downloadtimes = 0 where videono = '" + num + "'"
            cur.execute(sql)
            conn.commit()
            print(num + " magnetlink success")
        except Exception as ex:
            print(ex)
        finally:
            cur.close()
            conn.close()

conn=pymysql.connect(host=Config.HostIP,user=Config.UserName,passwd=Config.Password,db=Config.DBName,port=Config.Port,charset=Config.Charset)
cur=conn.cursor()
sql = "select videono from t_videos where status = 0"
cur.execute(sql)
for r in cur:
    try:
        getMagnet(r[0].strip())
    except Exception as ex:
        continue;
print("finish")
