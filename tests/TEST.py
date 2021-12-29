import requests
from scu_captcha import imgLoader,Predict # 只导入这两个需要的函数即可
from PIL import Image
# 本测试样例是从教务处拉取10张图片，并逐一对其进行识别，因为训练集不完全来自教务系统，所以只能说准确率尚可，目测可以达到90%以上，主要混淆来自于m和n的混淆
# 不一定每次都能成功，需要自行判断登录是否成功后，多次循环识别即可
captcha_url = "http://zhjw.scu.edu.cn/img/captcha.jpg"  # 验证码Url
# 伪装头
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Host': 'zhjw.scu.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3782.0 Safari/537.36 Edg/76.0.152.0'
}

def main():
    print("===模型装载完成===")
    session = requests.session()
    def downloadCaptcha(session):
        byte_Captcha = session.get(url=captcha_url, headers=header).content # 获取验证码的二进制数据
        
        # 保存图片到文件
        with open("captcha.jpg", "wb") as f:
            f.write(byte_Captcha)
        img = Image.open('captcha.jpg')
        img.show()
        
        '''
        =======以下是正确使用本识别包的一种方案，可以从相对路径中读取存储的图片======
        '''        
        # img = imgLoader("captcha.jpg")
        # res = Predict(img)
        '''
        ====以下是正确使用本识别包的另一种方案，可以直接从二进制码中读取存储的图片====
        '''        
        img = imgLoader(byte_Captcha)
        res = Predict(img)
        '''
        ======================================================================
        '''
        print(res)
        
    # 重复此过程10次    
    for i in range(10):
        downloadCaptcha(session)

if __name__ == "__main__":
    main()