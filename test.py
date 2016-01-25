import urllib2
import re
from os.path import basename
from urlparse import urlsplit

url = "http://tieba.baidu.com/p/683991021"
def getPage(url):
	url=url+"?see_lz=1"
	urlContent = urllib2.urlopen(url).read()
	page='<span class="red">(.*?)</span>'
	thePage=re.findall(page,urlContent)
	return int(thePage[0])
def downImg(url):
	urlContent = urllib2.urlopen(url).read()
	spans='<cc>(.*?)</cc>'
	ss=re.findall(spans,urlContent)
	obImgs=','.join(ss)
	imgUrls = re.findall('img .*?src="(.*?)"', obImgs)
	for imgUrl in imgUrls:
		try:
		    imgData = urllib2.urlopen(imgUrl).read()
		    fileName = basename(urlsplit(imgUrl)[2])
		    output = open(fileName,'wb')
		    output.write(imgData)
		    output.close()
		except:
		    print "Er.."
def downLoad(url):
	numb=getPage(url)
	cont=0
	print "There are "+str(numb)+" pages."
	while cont<numb:
		cont+=1
		print "Downloading "+url+"?see_lz=1&pn="+str(cont)+"..."
		downImg(url+"?see_lz=1&pn="+str(cont))
	print 'Completed!'
downLoad(url)
