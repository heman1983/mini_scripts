# 超级小的爬虫脚本
import requests
from bs4 import BeautifulSoup

def store_news(url,title):
    print(url,title)
# 爬取的目标url
url  = 'https://news.163.com/'
# 发起一个get请求
rsp = requests.get(url=url,verify=False)
html = rsp.text

# 重要节点，把网页需要的内容进行解析
soup = BeautifulSoup(html)

# 选择需要的节点
soup_elements = soup.select('.top_news_ul li a')
for item in soup_elements:
    new_url = item.get('href')
    new_title = item.string
    store_news(new_url,new_title)

# 知识点
# beatufulsoup 解析器
#### 如何获取指定的内容 类名 标签
#### 如何获取标签的属性 item.get('href')



