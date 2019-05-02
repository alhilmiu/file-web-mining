import re
import mainbasket_ambilfitur
import mainbasket_cekkamus
import mainbasket_cekstopword

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

import xlsxwriter

data = []
kumpulan_katadasar = ""
a=0

workbook = xlsxwriter.Workbook('mainbasket_daftarsteaming.xlsx')
worksheet1 = workbook.add_worksheet()

for kalimat in mainbasket_ambilfitur.data:
    a+=1
    print (a,">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print (kalimat)

    kalimat = kalimat.encode('utf-8').strip()

    factory = StopWordRemoverFactory()
    stopword = factory.create_stop_word_remover()
    stop = stopword.remove(kalimat)

    stop = re.sub(r'\b\w{1,2}\b', '', stop)

    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    katadasar = stemmer.stem(str(kalimat))
    katadasar = re.sub(r'\b\w{1,3}\b', '', katadasar).replace('-','')

    #seleksifitur
    temp_katadasar=''
    kalimat = katadasar.split(" ")
    for kata in kalimat:
        if (kata==""):
            continue

        elif (mainbasket_cekkamus.cek_kata(kata)==True and mainbasket_cekstopword.cek_kata(kata)==True):
            print ("y>>",kata)
            temp_katadasar=temp_katadasar+kata.strip()+" "
        else:
            print ("n >>", kata)
            continue
        #print (temp_katadasar)

    print(katadasar)
    print (temp_katadasar)
    data.append(temp_katadasar)

    kumpulan_katadasar = kumpulan_katadasar + temp_katadasar

    worksheet1.write(a, 1, str(kalimat))
    worksheet1.write(a, 2, str(temp_katadasar))

workbook.close()

temp = {}
kal = kumpulan_katadasar.split(" ")
for i in kal:
    if i not in temp:
        temp[i] = 1
    else:
        hasil_sementara = temp[i]
        temp[i] = hasil_sementara + 1


# print (temp)


def list_fitur():
    t = {}
    semua_kata = ""
    for i in data:
        semua_kata = semua_kata + i + " "

    for j in semua_kata.split(" "):
        t[j] = 0

    del t[""]
    return t


def coba1():
    tt = []

    for kalimat in data:
        list_kata = kalimat.split(" ")

        a = list_fitur()
        for kata in list_kata:
            if kata not in list_fitur():
                a[kata] = 0
            else:
                temp = a[kata]
                a[kata] = temp + 1

        tt.append(a)

        print (kalimat)

        print (a)
    return tt


print coba1()
print len(list_fitur())
print list_fitur()
print (str(coba1()[2].values()[1]))

