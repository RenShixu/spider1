import requests
import re

#数据准备
url = "http://bj.58.com/dashanzi/chuzu/pn1/?ClickID=1"
res = requests.get(url)
html = res.content.decode("utf-8")
#处理数据
pat = '<div class="img_list">.*?lazy_src="(.*?)".*?</div>.*?' \
      '<div class="des">.*?<h2>.*?<a.*?>(.*?)</a>.*?</h2>.*?<p class="room strongbox">(.*?)</p>.*?</div>.*?' \
      '<div class="listliright">.*?<b class="strongbox">([0-9]+)</b>.*?</div>'
contentlist = re.findall(pat,html,re.S)

for content in contentlist:
    print("标题："+content[1].strip()+"\n"+"户型："+content[2].replace(" ","").replace("&nbsp;"," ")+"\n"
          +"价格："+content[3]+"元/月"+"\n"+"图片地址："+content[0]+"\n-----------------------------")
print("共计："+str(len(contentlist))+"条")


