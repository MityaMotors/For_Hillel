




orders = session.query(Orders).all()

for order in orders:
    print(order)

