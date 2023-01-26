import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Juni031997")
cur  = conn.cursor()

with open("D:\\SUSI\\batch-processing-project-3\\source\\users_w_postal_code.csv",'r') as f:
    next(f)
    cur.copy_from(f,'latihan_user',sep=',',columns=('email','name','phone','postal_code'))
conn.commit()