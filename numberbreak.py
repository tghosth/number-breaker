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

def meta_redirect(content):
    "Get a meta refresh URL. From: http://stackoverflow.com/questions/2318446/how-to-follow-meta-refreshes-in-python"
    soup  = BeautifulSoup(content)

    result=soup.find("meta",attrs={"http-equiv":"refresh"})
    if result:
        wait,text=result["content"].split(";")
        if text.lower().startswith("url="):
            url=text[4:]
            return url
    return None


cookie_jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
urllib2.install_opener(opener)

urlString = 'http://s37109-102007-bxw.tarentum.hack.me/'

# acquire cookie
url_1 = urlString+'number.php'
req = urllib2.Request(url_1)
rsp = urllib2.urlopen(req)
rsp_html = rsp.read()
# print rsp_html



currNum = getcorrectnumbervalue(rsp_html)


# # do POST
url_2 = urlString+'proc.php '
values = dict(number=currNum, submit='submit')
data = urllib.urlencode(values)
req = urllib2.Request(url_2, data)
rsp = urllib2.urlopen(req)
content = rsp.read()

url = meta_redirect(content)

print content