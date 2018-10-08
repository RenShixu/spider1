from urllib import request
import re,os
def wirtetofile(contentlist,filepath,count):
    '''
    将信息写入文件
    :param contentlist:
    :param filepath:
    :return:
    '''
    try:
        if count == 0:
            file = open(filepath,"wb")
        else:
            file = open(filepath,"ab+")
        for content in contentlist:
            str = content[0]+"|"+content[2]+"|"+content[3].strip()+\
                  "|"+content[4]+"|"+content[5]+content[6]+"|"+content[1]+"\n"
            file.write(bytes(str,encoding="utf-8"))
            print(str)
        file.close()
        print("数据保存成功")
    except Exception as err:
        print(err)

#数据准备
heards = {
    'Accept - Language': 'zh - CN',
    'Connection': 'Keep - Alive',
    'Host':'maoyan.com',
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
}
count = 0
while True:
    url = "http://maoyan.com/board/4?offset=" +str(10*count)

    #爬取数据
    req = request.Request(url,headers=heards)
    res = request.urlopen(req)
    html = res.read().decode("utf-8")

    #数据处理
    pat1 = '<dd>.*?<i class="board-index board-index-[0-9]+">(.*?)</i>.*?' \
           '<img data-src="(.*?)@160w_220h_1e_1c" alt="(.*?)" class="board-img" />.*?' \
           '<p class="star">.*?主演：(.*?)</p>.*?<p class="releasetime">上映时间：([-0-9]+).*?</p>.*?' \
           '<i class="integer">([\.0-9]+)</i><i class="fraction">([0-9]+)</i>.*?</dd>'
    contentlist = re.findall(pat1,html,re.S)

    #保存信息到文件
    wirtetofile(contentlist,"D:/aaa.txt",count)

    #保存图片到本地
    i = 10 * count + 1
    imgspath = "D:/imgs"
    for content in contentlist:
        if not os.path.isdir(imgspath):
            os.mkdir(imgspath)
        request.urlretrieve(content[1],imgspath+"/{}.jpg".format(i))
        i = i + 1
    count = count + 1
    if count == 10:
        break

