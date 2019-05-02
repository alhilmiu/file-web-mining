import xlsxwriter
import xlrd
excel = xlrd.open_workbook("mainbasket_daftarsteaming.xlsx")
sheetdata = excel.sheet_by_index(0)
'''
data.name = nama sheet
data.nrows = jumah baris
data.ncols = jumlah kolom
'''


workbook = xlsxwriter.Workbook('mainbasket_vsmsatufitur.xlsx')
worksheet1 = workbook.add_worksheet()

data=[]
kumpulan_katadasar=""
for i in range(1,sheetdata.nrows):

    value = sheetdata.cell_value(rowx=i, colx=2)

    kumpulan_katadasar=kumpulan_katadasar+value
    data.append(value)

print (kumpulan_katadasar)


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
        #print (i)
        semua_kata = semua_kata + i + " "

    for j in semua_kata.split(" "):
        t[j] = 0

    del t[""]
    return t

print (len(list_fitur()))

print ((list_fitur()))

def hapus_fitur():
    temp=[]
    tampung_data=[]
    for baris in range(1, sheetdata.nrows):
       value = sheetdata.cell_value(rowx=baris, colx=2)
       tempkat = value.split(" ")
       tampung_data.append(tempkat)

    kolom=0
    for kata in list_fitur():
        count=0
        for i in range(len(tampung_data)):
            if kata in tampung_data[i] :
                count+=1

            if count>1:
                if kata not in temp:
                    temp.append(kata)
                    worksheet1.write(0,kolom+1,kata)


                kolom+=1

                break
    return temp

print ("panjang",len(hapus_fitur()))
print ("temp_fitur",(hapus_fitur()))



def hitung_katatiapbaris():
    tampung_data = []
    for baris in range(1, sheetdata.nrows):
        value = sheetdata.cell_value(rowx=baris, colx=2)
        temp = value.split(" ")
        dict_baris = {}
        for i in temp:
            if i == '':
                continue
            temp_count = 0

            for j in temp:

                if i == j:
                    temp_count += 1
            dict_baris[i] = temp_count
        tampung_data.append(dict_baris)

    return tampung_data

for baris in range(1,sheetdata.nrows):
    kolom=1
    for temp_fitur in hapus_fitur():

        if temp_fitur not in hitung_katatiapbaris()[baris-1]:
            hasil = 0
            #continue
        else:
            hasil=hitung_katatiapbaris()[baris-1][temp_fitur]

            print ("data ke>>",baris,"kata>>",temp_fitur,"ada>>",hasil)

        worksheet1.write(baris, kolom, int(hasil))

        kolom+=1
workbook.close()



