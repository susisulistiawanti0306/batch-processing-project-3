import psycopg2

#connect to postgresql
try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Juni031997")
    print("connect success")
except:
    print("An exception accured")

#menggunakan cursor
cur=conn.cursor()
cur.execute("select * from public.tabel_siswa")

#menampilkan hasil
all=cur.fetchall()
one=cur.fetchone()
conn.commit()

for record in all:
    print(str(record[0]) +"-"+ record[1])
