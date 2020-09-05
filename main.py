import requests
import os
import urllib.request
from bs4 import BeautifulSoup

#网页基地址
base_page_url = 'https://www.tujigu.com/a/5598/'
page_url_list = []

#所有网页保存至pata_url_list数组
for i in range(0, 15):
    url = base_page_url+str(i)+".html"
    page_url_list.append(url)
    #print(page_url_list[i])

#首先分割url 取list最后一个元素来当做我们的文件名,然后再下载到missA目录下
def download_image(url):
    split_list = url.split('/')
    filename = split_list.pop()
    path = os.path.join('D:\Download\missA', filename)
    urllib.request.urlretrieve(url, filename=path)

#解析页面的HTML源码 获取我们需要的部分
def get_page(page_url):
    response = requests.get(page_url)
    content = response.content
    soup = BeautifulSoup(content, 'lxml')
    img_list = soup.find_all('img', attrs={'class': 'tupian_img'})
    for img in img_list:
        url = img['src']
        download_image(url)

def main():
    #遍历数组
    for page_url in page_url_list:
        get_page(page_url)



if __name__ == "__main__":
    main()
