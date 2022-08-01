from contextlib import closing
import requests, os


def download_video(download_url, download_path):
    video_name = os.path.basename(download_path)
    with closing(requests.get(download_url, timeout=10, verify=False, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 文件总大小
        data_count = 0  # 当前已传输的大小
        with open(download_path, "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                done_block = int((data_count / content_size) * 50)  # 已经下载的文件大小
                data_count = data_count + len(data)  # 实时进度条进度
                now_jd = (data_count / content_size) * 100  # %% 表示%
                print("\r %s [%s%s] %d%% " % (
                    video_name + "---->", done_block * '█', ' ' * (50 - 1 - done_block), now_jd), end=" ")


if __name__ == '__main__':
    url = "https://cdn.kink.com/brutalsessions/members/102805/shoot/102805_shoot_low.mp4?nva=1659369973&token=d6347daeb1b9f9fd5f633b1fd6b15e03"
    video_path = "E:\\aa.mp4"
    download_video(url, video_path)
