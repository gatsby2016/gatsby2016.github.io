# encoding: utf-8
import urllib     # 导入urllib2模块  
import re         # 导入re模块  
import sys
reload(sys)
sys.setdefaultencoding("utf8")

# 转中文格式
def translate(str):
        line = str.strip().decode('utf-8', 'ignore')  # 处理前进行相关的处理，包括转换成Unicode等  
        p2 = re.compile(ur'[^\u4e00-\u9fa5]')  # 中文的编码范围是：\u4e00到\u9fa5  
        zh = " ".join(p2.split(line)).strip()
        zh = ",".join(zh.split())
        outStr = zh  # 经过相关处理后得到中文的文本  
        return outStr



for i in range(1,101):

	link = 'https://etmon.cc/super/' + str(i)
	# 读取link页面内容保存页面内容并读取
	page = urllib.urlopen(link)  
	html = page.read()
	# 正则匹配 reg 相似的 编译为imgre 并在html文件中寻找 
	reg = 'src="(.+?\.png)" type='
	imgre = re.compile(reg)
	answer = re.findall(imgre,html)[0]
	#if answer is None:
        #        continue;
	url = 'http://etmon.cc/' + answer
	name = answer.split('/static/svgs/super/')[-1].split('.png')[0]
	utf_name = translate(name)
	
	# 查找归属用户
	regg = '<span>(.*)</span>'
	imgree = re.compile(regg)
	user = re.findall(imgree,html)[1]
	if user[-3:] == 'eth':
		user = re.findall(imgree,html)[3]
		if user[-3:] == 'eth':
			user = '000'
	# 下载图片
	if user != '000':
		urllib.urlretrieve(url,'%s__%d__%s.png'%(user,i,utf_name))
		print link, '   ', user, i, utf_name,  '.....complete!'
	

