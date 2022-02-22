from homework_30.Repo.order_repo import OrderRepo

repository = OrderRepo()
orders = repository.get_all_orders()
# orders = repository.get_all_with_quantity_more(23)
#
# for order in orders:
#     print(order)

# order = repository.get_first_with_quantity_more(22)
# print(order)
# for order in orders:
#     print(order)

repository.add_order(
    {
        "id": "00000007",
        "product_id": "0000000077",
        "quantity": 77
    }
)
added_orders = repository.get_all_orders()
for order in added_orders:
    print(order)

# repository.change_quantity_for("00000002", 88)
#
# new_orders = repository.get_all_orders()
# for order in new_orders:
#     print(new_orders)


