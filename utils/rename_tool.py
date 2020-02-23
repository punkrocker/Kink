import os
from moviepy.editor import VideoFileClip


class RenameTool:
    def __init__(self, path):
        self.path = path

    def rename(self):
        for root, dirs, files in os.walk(self.path):
            path = root.replace(self.path, '').replace('\\', '-')
            for i in range(len(files)):
                file = files[i]
                if file.endswith('.mp4'):
                    full_file = os.path.join(root, file)
                    dest_file = os.path.join(root, path + '-' + str(i + 1) + '.mp4')
                    os.rename(full_file, dest_file)
                    print(full_file, dest_file)

    def get_video_length(self):
        file_dic = {}
        for root, dirs, files in os.walk(self.path):
            for i in range(len(files)):
                file = files[i]
                if file.endswith('.mp4'):
                    full_file = os.path.join(root, file)
                    clip = VideoFileClip(full_file)
                    file_time = clip.duration
                    file_dic[file] = file_time
                    clip.reader.close()
                    clip.audio.reader.close_proc()
        a = sorted(file_dic.items(), key=lambda x: x[1])
        for x in a:
            print(x)

    def time_convert(self, size):  # 单位换算
        M, H = 60, 60 ** 2
        if size < M:
            return str(size) + u'秒'
        if size < H:
            return u'%s分钟%s秒' % (int(size / M), int(size % M))
        else:
            hour = int(size / H)
            mine = int(size % H / M)
            second = int(size % H % M)
            tim_srt = u'%s小时%s分钟%s秒' % (hour, mine, second)
            return tim_srt


if __name__ == '__main__':
    renamer = RenameTool('H:\\china\\X-小鳥醬')
    renamer.get_video_length()
