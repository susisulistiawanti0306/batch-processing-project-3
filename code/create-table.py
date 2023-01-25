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

cur.execute("INSERT INTO latihan_user VALUES (%s, %s, %s, %s, %s)", (1, 'hello@dataquest.io', 'Some Name','621234413','1234'))
conn.commit()
print("Creat Table Success")
