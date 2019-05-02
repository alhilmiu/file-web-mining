import xlsxwriter

workbook = xlsxwriter.Workbook('mainbasket_daftarlinkberita.xlsx')
worksheet1 = workbook.add_worksheet()
kumpulan_link=[]

def cari_link(page):
    import urllib as link
    from bs4 import BeautifulSoup
    import re
    print (page)
    html_page = link.urlopen("https://www.mainbasket.com/c/4/berita/abl?page="+str(page)).read()
    soup = BeautifulSoup(html_page, "html.parser")

    for a in soup.findAll('div', 'post-title'):
        #print a
        for link in a.findAll('a', attrs={'href': re.compile("^https://")}):
            print link.get('href')
            kumpulan_link.append(link.get('href'))

for i in range(1,6):
    cari_link(str(i))
print len(kumpulan_link)

for baris in range(len(kumpulan_link)):
    print (baris)
    print (kumpulan_link[baris])
    worksheet1.write(baris,1, str(kumpulan_link[baris]))
workbook.close()
