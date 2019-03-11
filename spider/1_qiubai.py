# -*- coding: utf-8 -*-
# 目标: 使用python获取糗百的段子,并将段子显示到终端中,按回车查看下一个段子

import requests
from bs4 import BeautifulSoup

def getHtml(url):
  print "开始获取源网站代码"
  response=requests.get(url)
  response.enconding="utf-8"
  print "源代码已获取完成"
  return response.text

def getArticleList(content):
  print "开始获取文章列表"
  contentList=[]
  soup=BeautifulSoup(content,'html.parser')
  for article in soup.find_all('div',attrs={'class':'article'}):
    contentSpan=article.find_all("span")
    if contentSpan is None:
      continue
    content=contentSpan[0].get_text()
    authorTag=article.find_all("h2")
    if authorTag is None:
      continue
    author=authorTag[0].get_text()
    contentList.append({"author":author,"content":content})
  print "文章列表已获取完成,共计段子数:%d" % len(contentList)  
  return contentList  

page_index=1
while 1==1:
  html=getHtml("https://www.qiushibaike.com/hot/page/"+str(page_index)+"/")
  contentList=getArticleList(html)
  print "采集已完成."
  index=0
  while len(contentList)>index:
    userInput=raw_input('按(enter)退出请按(q/Q)显示第一条段子>:')
    content=contentList[index]
    if userInput =='':
      print "*"*100
      print "段子:",content["content"]
      print content["author"]
      print "*"*100
      
      index+=1
    elif userInput =='q' or userInput=='Q':
      print "大爷下次再来哦.."
      exit()
    else:
      continue
    page_index+=1
    continue




