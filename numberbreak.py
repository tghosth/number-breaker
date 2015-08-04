# __author__ = 'joshg'
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

    minval=1000000
    maxval=-1000000

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

def writetofile(filename, text):
    f = open(filename, 'a')
    f.write(text+'\n')
    f.close()

def usage():
    print 'WRONG FLAGS!!!!!!'

def processargs(argv):
    try:
        opts, args = getopt.getopt(argv, "u:of:", ["url=", "output", "file="])

    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-u", "--url"):
            print "urlString = "+ arg
            global urlString
            urlString = arg
        elif opt in ("-o","--output"):
            print "DoOutput = True"
            global DoOutput
            DoOutput = True
        elif opt in ("-f","--file"):
            global OutputFile
            print "OutputFile = "+ arg
            OutputFile = arg
    return;

global urlString
urlString = ""
global OutputFile
OutputFile= ""
global DoOutput
DoOutput = False

processargs(sys.argv[1:])

if urlString == "": urlString = 'http://s37109-102007-bxw.tarentum.hack.me/'
if (OutputFile == "") and (DoOutput): OutputFile = os.path.dirname(os.path.abspath(__file__)) + '\output.txt'


if os.path.isfile(OutputFile):
    print 'FILE: "' + OutputFile + '" already exists!'
    sys.exit(2)


cookie_jar = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_jar))
urllib2.install_opener(opener)



# acquire cookie
rsp_html = getrequest(urlString+'number.php')
# print rsp_html


while True:

    if DoOutput: writetofile(OutputFile, rsp_html+"\n\n\n")

    currNum = getcorrectnumbervalue(rsp_html)

    if DoOutput: writetofile(OutputFile, "Number sent: " + str(currNum) + "\n\n\n")


    content = postrequest(urlString+'proc.php ', dict(number=currNum, submit='submit'))

    if DoOutput: writetofile(OutputFile, content+"\n\n\n")

    rsp_html = getrequest(urlString+'number.php')

