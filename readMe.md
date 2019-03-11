> 一些python的小练习

`spider/1_wallhaven.py` 下载 壁纸网站`wallhaven`中的韩国妹子(列表小图)
使用 `requests` 和 `Beautifulsoup`

效果截图在`spider/wallhaven_images`文件夹中


`spider/2_wallhaven_big_images.py` 下载 壁纸网站`wallhaven`中的韩国妹子(列表对应的大图)

`spider/3_wallhaven_big_mulit_process.py` 下载 壁纸网站`wallhaven`中的韩国妹子(上一个例子的多线程版本)
多线程的速度快很多

`spider/1_qiubai.py` 抓取糗百的段子,根据用户需要将内容显示在终端上(自动分页获取段子,图片暂未解析)