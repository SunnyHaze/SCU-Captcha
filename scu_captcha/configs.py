import torch
from matplotlib import pyplot as plt
import torchvision.transforms as transforms

charRange = '2345678abcdefgmnpwxy' # 川大JWC的验证码只涉及这些字符
charRangeLength = len(charRange) # 输出向量的长度
# 首先构造字符到下标的散列表
char2idx = {charRange[i] : i for i in range(charRangeLength)}

# 配置读取器
loader = transforms.Compose([transforms.ToTensor()])
unloader = transforms.ToPILImage()

def tensor2token(vec : torch.Tensor):
    row =vec.tolist()
    ans = ""
    for i in range(charRangeLength * 4):
        if row[i] == 1:
            ans = ans + charRange[i % charRangeLength]
    return ans
    
def imshow(inp, title = None):
    inp = unloader(inp)
    plt.imshow(inp)
    if title is not None:
        plt.title(title)
    plt.pause(5)  # pause a bit so that plots are updated

    
if __name__ == "__main__":
    print("Output vector length: " + str(charRangeLength))
    print("Hash Dict for characters:")
    print(char2idx)