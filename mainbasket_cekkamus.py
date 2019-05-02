def cek_kata(kata):
    doc=open("kata-dasar.txt","r")
    kumpulan_kata=doc.read()
    #print (kumpulan_kata)


    if kata in kumpulan_kata:
        ketemu=True
    else:
        ketemu=False

    return ketemu
