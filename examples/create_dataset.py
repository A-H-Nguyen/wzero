import numpy as np
import os

import wzero.datasets.utils as utils

download_folder = '/root/wzero_datasets/mnist/'

x_train_path = 'train-images-idx3-ubyte.gz'
y_train_path = 'train-labels-idx1-ubyte.gz'
x_test_path = 't10k-images-idx3-ubyte.gz'
y_test_path = 't10k-labels-idx1-ubyte.gz'

x_train = utils.load_ubyte(x_train_path, 60000, (28, 28), 16)
y_train = utils.load_ubyte(y_train_path, 60000, (), 8)
x_test = utils.load_ubyte(x_test_path, 10000, (28, 28), 16)
y_test = utils.load_ubyte(y_test_path, 10000, (), 8)

# os.remove(x_train_path)
# os.remove(y_train_path)
# os.remove(x_test_path)
# os.remove(y_test_path)

np.save(os.path.join(download_folder, 'x_train.npy'), x_train)
np.save(os.path.join(download_folder, 'y_train.npy'), y_train)
np.save(os.path.join(download_folder, 'x_test.npy'), x_test)
np.save(os.path.join(download_folder, 'y_test.npy'), y_test)
