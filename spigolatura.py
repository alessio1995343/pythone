#prende l'url di un sito e printa l'html
import urllib.request
url ="https://www.fromsoftware.jp/ww/"
risultato = urllib.request.urlopen(url)
theBytes = risultato.read()
text = theBytes.decode()
import bs4 
doc = bs4.BeautifulSoup(text)
print (doc.prettify())
#mostra tutti i tag del html e li printa con la gerarchia 
def naviga2 (tag,indent):
    print (indent +tag.name.upper())
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag:
            naviga2 (stag,indent + "  ")

naviga2(doc, "  ") 
