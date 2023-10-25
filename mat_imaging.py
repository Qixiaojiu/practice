import os
import h5py
import scipy.io as scio
import numpy as np


datapath = 'E:\\1\\code\\data_process\\data\\public_mat'
datadir = os.listdir(datapath)

for classname in datadir:
    matdir = os.path.join(datapath, classname)
    matname = os.listdir(matdir)[0]
    loadmat = h5py.File(os.path.join(matdir, matname), 'r')
    data = np.array((loadmat['adcRawData']['data']))
    m = len(data)
    for i in range(0,m):
        data_group = h5py.File(data[i], 'r')
    # 20231025