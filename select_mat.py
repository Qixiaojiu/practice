#从多个文件夹中提取.mat文件

import os
import shutil

filepath = 'E:\\1\\data\\imaging'
dirpath = './data/public_mat/'

dirlist = os.listdir(filepath)
for dir1 in dirlist:
    #判断是否是文件夹
    old_datapath = os.path.join(filepath, dir1)
    if os.path.isdir(old_datapath):
        filelist = os.listdir(old_datapath)
        # for file in range(len(filelist)):
        for file in filelist:
            if file.split('.')[1] == 'mat':
                name = dir1.split('_')[1] + dir1.split('_')[2]
                new_datapath = os.path.join(dirpath, name)
                if not os.path.exists(new_datapath):
                    os.makedirs(new_datapath)
                shutil.copy(os.path.join(old_datapath, file), os.path.join(new_datapath, file))