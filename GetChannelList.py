from bs4 import BeautifulSoup
import pymysql
import Config

user_agent = 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent, 'Cookie': 'viewing-preferences=straight'}


def parse_html(all_the_text):
    soup = BeautifulSoup(all_the_text, "html.parser")
    channels = soup.findAll("div", {"class", "new-channel-tile"})
    conn = pymysql.connect(host=Config.HostIP, user=Config.UserName, passwd=Config.Password, db=Config.DBName,
                           port=Config.Port, charset=Config.Charset)
    cur = conn.cursor()
    for channel in channels:
        query = ('insert into T_Channel (ChannelName) values(%s)')
        cur.execute(query, (channel['data-title']))
        conn.commit()  # 只要是修改了表内容的操作，后面一定要提交，否则不起作用
    cur.close()
    conn.close()


if __name__ == '__main__':
    content = open('./target_html/channel.html', 'r', encoding='utf-8').read()
    parse_html(content)
