import psycopg2

connection = psycopg2.connect(database="umuzi_pcs", user="user", password="pass", host="localhost", port=8000)