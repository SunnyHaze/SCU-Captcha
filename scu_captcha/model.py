import torch.nn.functional as F
from scu_captcha.configs import *
import torch.nn as nn

numClasses = charRangeLength * 4
imageSize = (180,60)

depth = [4,8]
class ConvNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3,depth[0],5,padding=2)
        self.pool = nn.MaxPool2d(2,2)
        self.conv2 = nn.Conv2d(depth[0],depth[1],5,padding=2)
        self.fc1 = nn.Linear(depth[1] * imageSize[0] // 4 * imageSize[1] // 4,512)
        self.fc2 = nn.Linear(512,numClasses)

    def forward(self,x):
        x = F.relu(self.conv1(x))  #第一层卷积的激活函数用ReLu
        x = self.pool(x) #第二层pooling，将片变小
        
        x = F.relu(self.conv2(x)) #第三层卷积，输入输出通道分别为depth[0]=4, depth[1]=8
        x = self.pool(x) #第四层pooling，将图片缩小到原大小的1/4
        
        x = x.view(-1, imageSize[0] // 4 * imageSize[1] // 4 * depth[1])
        
        x = F.relu(self.fc1(x)) #第五层为全链接，ReLu激活函数
        
        x = F.dropout(x, training=self.training) #以默认为0.5的概率对这一层进行dropout操作，为了防止过拟合
        x = self.fc2(x) 
        
        x = F.log_softmax(x, dim = 0) 
        return x