import psycopg2

connection = psycopg2.connect(
    database="mydb",
    host="localhost",
    port="5432",
    user="postgres",
    password="mitya232"
)
cursor = connection.cursor()
cursor.execute("SELECT * FROM orders;")

orders = cursor.fetchall()

print(orders)

for order in orders:
    print(order)
cursor.close()
connection.close()
