__author__ = 'joshg'
import urllib, urllib2, cookielib
from bs4 import BeautifulSoup

def getcorrectnumbervalue(htmltext):
    "Parses the HTML text and gets out the required number"

    parsed_html = BeautifulSoup(htmltext,"html.parser")

    print parsed_html.body.form.p

    numberstringminmax = parsed_html.body.form.p.text

    numberstring = numberstringminmax.decode("utf-8").replace(u'The minimum number?',u'')

    maxnum = True

    if len(numberstring) != len(numberstringminmax.decode("utf-8")):
        maxnum = False
    else:
        maxnum = True
        numberstring = numberstringminmax.decode("utf-8").replace(u'The maximum number?',u'')

    minval=0
    maxval=0

    for currNum in numberstring.split(", "):
        if int(currNum) > maxval: maxval = int(currNum)
        if int(currNum) < minval: minval = int(currNum)

    finalval = 0

    if maxnum:
        finalval=maxval
    else:
        finalval=minval

    return finalval;


cookie_jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
urllib2.install_opener(opener)

# acquire cookie
url_1 = 'http://s37109-102007-bxw.tarentum.hack.me/number.php'
req = urllib2.Request(url_1)
rsp = urllib2.urlopen(req)
rsp_html = rsp.read()
# print rsp_html





print str(getcorrectnumbervalue(rsp_html))



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