import psycopg2

#connect to postgresql
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=Juni031997")
cur = conn.cursor()
 
#create table
cur.execute("""
                CREATE TABLE IF NOT EXISTS latihan_user(
                    id serial PRIMARY KEY,
                    email text,
                    name text,
                    phone text,
                    postal_code text
                )
    """
    )

import csv
with open("D:\\SUSI\\batch-processing-project-3\\source\\users_w_postal_code.csv") as f:
    csv_reader = csv.reader (f, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        cur.execute("INSERT INTO latihan_user VALUES ( default, %s, %s, %s, %s) ON CONFLICT DO NOTHING", row)
        
conn.commit()
#print("Creat Table Success")
