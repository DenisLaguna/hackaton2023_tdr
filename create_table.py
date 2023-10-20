import psycopg2

HOST_IP = '127.0.0.8'
PORT = 5432
POSTGRES_USER = 'root'
POSTGRES_PASSWORD = 'root'
POSTGRES_DP = 'hackaton2023'

conn = psycopg2.connect(host=HOST_IP, port=PORT, database = POSTGRES_DP, user=POSTGRES_USER, password=POSTGRES_PASSWORD)
cur = conn.cursor()
cur.execute("CREATE TABLE users (user_id serial PRIMARY KEY, login VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL);")
conn.commit()

cur.execute("CREATE TABLE ticket (ticket_id serial PRIMARY KEY, train VARCHAR(255) NOT NULL, car VARCHAR(255) NOT NULL, place VARCHAR(255) NOT NULL, fullname VARCHAR(255) NOT NULL, passnomber VARCHAR(255) NOT NULL, passseries VARCHAR(255) NOT NULL);")
conn.commit()
conn.close()
cur.close()

