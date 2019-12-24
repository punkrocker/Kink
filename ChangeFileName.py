# 修改Kink原始文件名，添加系列
import os

for filename in os.listdir('G:\\'):
    if not os.path.isdir(filename) and filename.endswith('.mp4'):
        print(filename)
