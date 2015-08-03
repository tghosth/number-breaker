__author__ = 'joshg'
import urllib, urllib2, cookielib, os.path, sys, getopt
from bs4 import BeautifulSoup

def getcorrectnumbervalue(htmltext):
    "Parses the HTML text and gets out the required number"

    parsed_html = BeautifulSoup(htmltext,"html.parser")

    print parsed_html.body.form.p

    print 'Score: ' + parsed_html.body.div.p.text.split("Score:")[1]

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

def getrequest( url ):
    req = urllib2.Request(url)
    rsp = urllib2.urlopen(req)
    return rsp.read();

def postrequest( url, values ):
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    rsp = urllib2.urlopen(req)
    return rsp.read();


def usage():
    print 'WRONG FLAGS!!!!!!'

def processargs(argv):
    try:
        opts, args = getopt.getopt(argv, "u:", ["url="])

    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-u", "--url"):
            print "urlString = "+ arg
            global urlString
            urlString = arg
    return;

global urlString
urlString = ""


processargs(sys.argv[1:])

if urlString == "": urlString = 'http://s37109-102007-bxw.tarentum.hack.me/'



cookie_jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
urllib2.install_opener(opener)



# acquire cookie
rsp_html = getrequest(urlString+'number.php')
# print rsp_html


while True:
    currNum = getcorrectnumbervalue(rsp_html)

    content = postrequest(urlString+'proc.php ', dict(number=currNum, submit='submit'))

    rsp_html = getrequest(urlString+'number.php')

