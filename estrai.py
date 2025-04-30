
import urllib.request
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")

import bs4
doc = bs4.BeautifulSoup(text, "html.parser")
elems = doc.find_all("table")
table = elems[3] 
for tr in table.contents[2:-1]:
    if type(tr) == bs4.element.Tag:
        tds = tr.contents
        prov=   (tds[1]).get_text()
        resi=int((tds[2]).get_text().replace(".",""))
        sigl=   (tds[7]).get_text()
        sup= int((tds[4]).get_text().replace(".",""))
        den=float((tds[5]).get_text().replace(",",""))
        densita=resi/sup
        denfinale= round(densita, 1)
        if (denfinale==den):
         print(f"{sigl} {prov:25s} {resi:9d} {sup:4d} {den}")
        else:
            print("la densità calcolata è diversa da quella riportata in tabella")
            print(f"{sigl} {prov:25s} {resi:9d} {sup:4d} {denfinale}")

    






def naviga2 (tag,indent):
    print (indent +tag.name.upper())
    print(tag.get_attribute_list)
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag:
            naviga2 (stag,indent + "  ")
