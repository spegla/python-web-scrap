import urllib
import re

urls =



htmlfile = urllib.urlopen('http://finance.yahoo.com/quote/AAPL?p=AAPL')

htmltext = htmlfile.read()

regex = '<span class="Fw(b) D(ib) Fz(36px) Mb(-4px)" data-reactid=".1jqy6gkx0qg.0.$0.0.0.3.1.$main-0-Quote-Proxy.$main-0-Quote.0.1.0.$price.0">(.+?)</span>'

pattern = re.compile(regex)

price = re.findall(pattern,htmltext)

print price