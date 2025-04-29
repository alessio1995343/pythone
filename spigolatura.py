import urllib.request
url ="https://www.fromsoftware.jp/ww/"
risultato = urllib.request.urlopen(url)
theBytes = risultato.read()
text = theBytes.decode()
import bs4 
doc = bs4.BeautifulSoup(text)
print (doc.prettify())