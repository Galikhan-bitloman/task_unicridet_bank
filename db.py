import psycopg2
from parse import split_data


conn = psycopg2.connect(dbname="postgres",
                        user="postgres",
                        password="Apple123",
                        host="localhost",
                        port="5432"
                        )
cur = conn.cursor()



data_from_split_data = split_data("https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
for i in data_from_split_data:
    cur.execute("insert into data1 (datas) VALUES (%s); ", (i,))


conn.commit()



conn.close()
cur.close()

