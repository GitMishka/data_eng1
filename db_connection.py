import psycopg2

conn = psycopg2.connect("dbname=test user=postgres")

cur = conn.cursor()

cur.execute("SELECT * FROM my_table")

records = cur.fetchall()
