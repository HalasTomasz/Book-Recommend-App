
import psycopg2

conn = psycopg2.connect('postgres://fshnrvmtnplkxx:4948725e7f7c0fde1edc4ea7574750e8168e0c1e4fe2226c19fba72bad0bf1ee@ec2-52-73-184-24.compute-1.amazonaws.com:5432/d3stbt3tnperuh', sslmode='require')
cur=conn.cursor()
print(cur.execute("SELECT * FROM base_userreview "))
