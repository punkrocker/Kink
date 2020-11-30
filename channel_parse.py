from bs4 import BeautifulSoup
import pymysql
import Config
from dto.channel import Channel


class ChannelParse:
    def parse_html(self, all_the_text):
        soup = BeautifulSoup(all_the_text, "html.parser")
        channel_tiles = soup.findAll("div", {"class", "new-channel-tile"})
        channels = []
        for tile in channel_tiles:
            channel = Channel()
            channel.name = tile['data-title']
            channel.url = tile.find("a")['href']
            channels.append(channel)
        return channels

    def save_to_db(self, channels):
        conn = pymysql.connect(host=Config.HostIP, user=Config.UserName, passwd=Config.Password, db=Config.DBName,
                               port=Config.Port, charset=Config.Charset)
        cur = conn.cursor()
        for channel in channels:
            query = ('insert into T_Channel (ChannelName, ChannelUrl) values(%s, %s)')
            cur.execute(query, (channel.name, channel.url))
            conn.commit()  # 只要是修改了表内容的操作，后面一定要提交，否则不起作用
        cur.close()
        conn.close()


if __name__ == '__main__':
    content = open('./target_html/channel.html', 'r', encoding='utf-8').read()
    chs = ChannelParse()
    for ch in chs.parse_html(content):
        print(ch.name, ch.url)
