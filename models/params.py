import torch
from torchvision.models import resnet50
import numpy as np
from models.model import RefineNet
from models.model import Bottleneck
Total_params = 0
Trainable_params = 0
NonTrainable_params = 0

model = RefineNet(Bottleneck, [3, 4, 23, 3])
for param in model.parameters():
    mulValue = np.prod(param.size())  # 使用numpy prod接口计算参数数组所有元素之积
    Total_params += mulValue  # 总参数量
    if param.requires_grad:
        Trainable_params += mulValue  # 可训练参数量
    else:
        NonTrainable_params += mulValue  # 非可训练参数量

print(f'Total params: {Total_params / 1e6}M')
print(f'Trainable params: {Trainable_params/ 1e6}M')
print(f'Non-trainable params: {NonTrainable_params/ 1e6}M')

