# -*- coding: utf-8 -*-
# 目标: 使用python下载 wallhaven中的韩国妹子(小图)
import requests
from bs4 import BeautifulSoup
def getHtml():
  print "开始获取源网站代码"
  response=requests.get("https://alpha.wallhaven.cc/search?q=korean+girl&categories=111&purity=100&sorting=relevance&order=desc&page=4")
  response.enconding="utf-8"
  # print "response.text",response.text
  print "源代码已获取完成"
  return response.text

def getImageLists(html):
  print "寻找源码中的图片地址"
  images=[]
  soup=BeautifulSoup(html,'html.parser')
  for figure in soup.find_all('figure'):
    if figure is None:
      continue
    img=figure.find_all('img')
    if img is None:
      continue
    img_url=img[0].get('data-src')
    images.append(img_url)
  print "源码中的图片地址已经全部找出"
  return images  

def downLoadImages(images):
  print "准备下载图片 共计%d张图片" % len(images)
  index=0
  for img in images:
    index+=1
    file_name=img.split('/')[-1]
    print file_name,"下载中..."
    response=requests.get(img)
    content=response.content
    with open('./wallhaven_images/'+file_name,'wb') as fs:
      fs.write(content)
    print file_name,"下载完成"
    print "已下载图片数量:%d,还有图片:%d" % (index,len(images)-index)


html=getHtml()
images=getImageLists(html)
downLoadImages(images)

