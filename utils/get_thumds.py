import os, shutil

path_origin = 'F:\\迅雷下载\\9-28-i'
for root, dirs, files in os.walk(path_origin):
    path = root.replace(path_origin, '').replace('\\', '-')
    for i in range(len(files)):
        file = files[i]
        if file.endswith('.jpg'):
            full_file = os.path.join(root, file)
            # dest_file = os.path.join(root, path + '-' + str(i + 1) + '.jpg')
            # os.rename(full_file, dest_file)
            dest_file = os.path.join(path_origin, path + "-" + str(i + 1) + '.jpg')
            shutil.copy2(full_file, dest_file)
            print(full_file, dest_file)
