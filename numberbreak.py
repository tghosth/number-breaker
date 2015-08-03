__author__ = 'joshg'
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup

cookie_jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
urllib2.install_opener(opener)

# acquire cookie
url_1 = 'http://s37109-102007-bxw.tarentum.hack.me/number.php'
req = urllib2.Request(url_1)
rsp = urllib2.urlopen(req)
rsp_html = rsp.read()
# print rsp_html


parsed_html = BeautifulSoup(rsp_html,"html.parser")

print "Parsed version:"
numberStringMinMax = parsed_html.body.form.p.text

numberString = numberStringMinMax.decode("utf-8").replace(u'The minimum number?',u'')

maxNum = True

if len(numberString) != len(numberStringMinMax.decode("utf-8")):
    maxNum = False
else:
    maxNum = True
    numberString = numberStringMinMax.decode("utf-8").replace(u'The maximum number?',u'')

print numberString.split(", ")

minVal=0
maxVal=0



# .toString()
# .split('<br/>')


# # do POST
# url_2 = 'http://www.bkstr.com/webapp/wcs/stores/servlet/BuybackSearch'
# values = dict(isbn='9780131185838', schoolStoreId='15828', catalogId='10001')
# data = urllib.urlencode(values)
# req = urllib2.Request(url_2, data)
# rsp = urllib2.urlopen(req)
# content = rsp.read()

# print content