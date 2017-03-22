import urllib.request  # 网络访问模块
import random  # 随机数生成模块
import re  # 正则表达式模块
import os  # 目录结构处理模块

# 初始化配置参数
number = 10  # 图片收集数量
path = '/Users/costa92/Documents/img/'  # 图片存放目录


# 文件操作
if not os.path.exists(path):
	os.makedirs(path)
	


# 图片保存
def save_img(url, path):
	message = None
	try:
		file = open(path + os.path.basename(url), 'wb')
		request = urllib.request.urlopen(url)
		file.write(request.read())
	except Exception as e:
		message = str(e)
	else:
		message = os.path.basename(url)
	finally:
		if not file.closed:
			file.close()
		return message


# 网络连接
http = 'http://zerospace.asika.tw/photo/'  # 目标网址
position = 290 + int((1000 - number) * random.random())
ids = range(position, position + number)

for id in ids:
	try:
		url = "%s%d.html" % (http, id)  # 后缀生成
		request = urllib.request.urlopen(url)
	except Exception as e:
		print(e)
		continue
	else:
		buffer = request.read()
		buffer = buffer.decode('utf8')
		pattern = 'class="content-img".+\s+.+src="(.+\.jpg)"'
		imgurl = re.findall(pattern, buffer)  # 过滤规则
		if len(imgurl) != 0:
			print(save_img(imgurl[0],path))
		else:
			 continue
	pass			
	    