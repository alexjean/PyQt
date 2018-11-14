# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 下午 6:17
# @Author  : AlexJean
import torch
import numpy
x=torch.FloatTensor(5,3)
print(x)
print(x.size())
y=torch.rand(5,3)
print(y)
print('----- x+y ------')
print(x+y)
print('----- add(x,y) ------')
print(torch.add(x,y))
print('----- torch.ones(5) -----')
a=torch.ones(5)
print(a)
b=a.numpy()
print(b)