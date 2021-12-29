from io import BytesIO
from torch.functional import Tensor
from scu_captcha.model import *
from PIL import Image
import os
import torch
WORK_PATH = os.path.dirname(__file__)
# 加载模型
cnnNet =ConvNet()
model_PKT = torch.load(os.path.join( WORK_PATH,"model.pt"),map_location=torch.device('cpu'))
cnnNet.load_state_dict(model_PKT["state_dict"])
cnnNet.eval() # 调整为评估模式

# 支持路径输入与二进制直接输入
def imgLoader(ImgObject) -> Tensor:
    if isinstance(ImgObject,str): 
        img = Image.open(ImgObject)
    if isinstance(ImgObject,bytes):
        img = Image.open(BytesIO(ImgObject))
    return loader(img)

# 创建Dataloader
def createLoader(ImageTensor:Tensor):
    preData = torch.load(os.path.join( WORK_PATH,"preData.pt"))
    imglist = preData[:8] + [ImageTensor] + preData[8:]
    return torch.utils.data.DataLoader(imglist,batch_size=16)
# 获取最终预测的向量
def getPredictTensor(predictions):
    res = predictions.detach().clone()
    predChunk = torch.chunk(res,dim = 1, chunks=4)
    for i in range(len(predChunk)):
        pre = torch.max(predChunk[i].data,1)[1]
        predChunk[i].zero_()
        for j in range(pre.shape[0]):
            predChunk[i][j,pre[j]] = 1      

    res = predChunk[0]
    for i in range(1,4):
        res =  torch.cat([res,predChunk[i]], dim = 1)
    return res
# 进行预测
def Predict(imageTensor):
    Testloader = createLoader(imageTensor)
    for i in Testloader:
        output = cnnNet(i)
    prediction = getPredictTensor(output)
    result = tensor2token(prediction[8])
    return result
    
