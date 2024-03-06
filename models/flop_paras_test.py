from torchvision.models import resnet50 # Introduce the ResNet50 model
from thop import profile
import torch
from models.model import RefineNet
from models.model import Bottleneck




from thop import profile
model = RefineNet(Bottleneck, [3, 4, 23, 3])
input = torch.randn(1, 1, 224, 224)
flops, params = profile(model, inputs=(input, ))# flops单位G，para单位M
print("%.2fG"% (flops/1e9), "%.2fM"% (params/1e6))