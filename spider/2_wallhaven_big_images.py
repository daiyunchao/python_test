# -*- coding: utf-8 -*-
# 目标: 使用python下载 wallhaven中的韩国妹子(大图)
import requests
from bs4 import BeautifulSoup

# 获取url的HTML


def getHtml(url):
    print "开始获取源网站代码"
    response = requests.get(url)
    response.enconding = "utf-8"
    # print "response.text",response.text
    print "源代码已获取完成"
    return response.text

# 从详情html中获取大图的url


def getBigImageUrlByBigImageHtml(html):
    url = ""
    # print "html: %s" %html
    soup = BeautifulSoup(html, 'html.parser')
    section = soup.find_all('section')
    if section is None:
        return url
    img = section[0].find_all('img')
    if img is None:
        return ""
    url = img[0].get('src')
    url = "https:"+url
    return url


# 获取大图片的链接
def getBigImagsLinks(html):
    print "寻找源码中找到打开大图的地址"
    imgUrlLink = []
    soup = BeautifulSoup(html, 'html.parser')
    for figure in soup.find_all('figure'):
        if figure is None:
            continue
        a = figure.find_all('a')
        if a is None:
            continue
        a_link = a[0].get('href')
        imgUrlLink.append(a_link)
    print "寻找源码中找到打开大图的地址完成"
    return imgUrlLink

# 获取大图片列表


def getImageLists(links):
    print "开始获取图片的URL列表"
    print "共计获取到链接数量为:%d" % len(links)
    index = 0
    images = []
    for link in links:
        index += 1
        print link
        print "当前获取第%d张大图" % index
        link_html = getHtml(link)
        image = getBigImageUrlByBigImageHtml(link_html)
        print "获取到的大图地址:", image
        images.append(image)
    return images


def downLoadImages(images):
    print "准备下载图片 共计%d张图片" % len(images)
    index = 0
    for img in images:
        index += 1
        print "正在下载:", img
        file_name = img.split('/')[-1]
        print file_name, "下载中..."
        response = requests.get(img)
        content = response.content
        with open('./wallhaven_images/'+file_name, 'wb') as fs:
            fs.write(content)
        print file_name, "下载完成"
        print "已下载图片数量:%d,还有图片:%d" % (index, len(images)-index)


html = getHtml(
    'https://alpha.wallhaven.cc/search?q=korean+girl&categories=111&purity=100&sorting=relevance&order=desc&page=4')
links = getBigImagsLinks(html)
images = getImageLists(links)
downLoadImages(images)
