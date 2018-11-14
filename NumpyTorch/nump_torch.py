# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 上午 11:05
# @Author  : AlexJean

import torch
import numpy as np

np_data = np.arange(6).reshape((2,3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()

print(np_data, '\nnumpy=>torch', torch_data,
      'tensor2array\n', tensor2array)


data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)

print('numpy==>\n', np.matmul(data, data),
      '\n\ntorch==>', torch.matmul(tensor,tensor))
