import sqlite3
conn = sqlite3.connect('mainbasket.db')
c = conn.cursor()

c.execute('SELECT * FROM berita_abl')

rows = c.fetchall()

data=[]
for row in rows:
    baris=""
    for j in row:
        j=j.replace(',', '')
        baris=baris+j+" "

    data.append(baris)

#for i in data:
#    print i
