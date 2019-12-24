import os

for filename in os.listdir('G:\\'):
    if not os.path.isdir(filename) and filename.endswith('.mp4'):
        print(filename)
