import psycopg2

conn = psycopg2.connect(
    dbname="products",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()


