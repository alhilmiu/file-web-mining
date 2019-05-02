def cek_kata(kata):
    doc=open("stopwords.txt","r")
    kumpulan_kata=doc.read()
    #print (kumpulan_kata)


    if kata not in kumpulan_kata:
        ketemu=True
    else:
        ketemu=False

    return ketemu
