
import urllib
import re

urls = ["http://www.b92.net/","http://www.blic.rs/","http://www.kurir.rs/","http://nytimes.com"]

i = 0
regextitle = '<title>(.+?)</title>'
regexH = '<h1>(.+?)</h1>'

pattern = re.compile(regextitle)
patternH = re.compile(regexH)

while i< len(urls):

    htmlfile = urllib.urlopen(urls[i])
    htmltext = htmlfile.read()
    titles = re.findall(pattern,htmltext)
    titleH = re.findall(patternH,htmltext)

    print titles + titleH
    i += 1
