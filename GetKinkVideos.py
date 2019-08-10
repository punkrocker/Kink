from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import urllib
import pymysql
import Config

try:
    user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
    headers = { 'User-Agent' : user_agent , 'Cookie':'viewing-preferences=straight'}
    url = "http://www.kink.com/shoots/latest"
    req = urllib.request.Request(url,None,headers)
    all_the_text = urlopen(req).read()
except HTTPError as e:
    print(e)
else:
    soup = BeautifulSoup(all_the_text, "html.parser")
    result = soup.find("div",{"class","shoot-list"})
    shoots = result.findAll("div",{"class","shoot"})
    for child in shoots:
        try:
            performer = child.find("div",{"class","shoot-thumb-models"}).get_text().strip()
            videoName = child.find("div",{"class","script"}).get_text().strip()
            videoNo = child.a.get("href").replace("/shoot/","")
            pic = child.find("img",{"class","adimage"}).get("src")
            if (not pic.startswith("http")):
                continue;
            try:
                conn = pymysql.connect(host=Config.HostIP,user=Config.UserName,passwd=Config.Password,db=Config.DBName,port=Config.Port,charset=Config.Charset)
                cur = conn.cursor()
                sql = "select count(1) as num from t_videos where videono = '" + videoNo + "'"
                cur.execute(sql)
                r = cur.fetchall()
                if (r[0][0] > 0):
                    continue
                else:
                     #下载图片
                    try:
                        path = Config.Path
                        pic_location = path + videoNo + ".jpg"
                        picconn = urllib.request.urlopen(pic)
                        f = open(pic_location,'wb')
                        f.write(picconn.read())
                        f.close()
                    except HTTPError as e:
                        print(e)
                sql = "insert into t_videos (companyname,videono,status,performer,img,videoname) values ('Kink','" + videoNo.replace('\'','\\\'') + "','0','" + performer.replace('\'','\\\'')  + "','" + videoNo + ".jpg" + "',' " + videoName.replace('\'','\\\'')  + " ')"
                cur.execute(sql)
                conn.commit()
                print(videoNo + ":SUCCESS")
            except Exception as ex:
                print(ex)
            finally:
                cur.close()
                conn.close()
        except  Exception as e :
            print(e)
print("finish")