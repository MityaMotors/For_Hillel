from typing import List

from homework_30.core.base_repo import BaseRepo
from homework_30.models.order import Order


class OrderRepo(BaseRepo):
    def get_all_orders(self) -> List[Order]:
        return self._session.query(Order).all()

    def get_all_with_quantity_more(self, quantity: int) -> List[Order]:
        return self._session.query(Order).filter(Order.quantity > quantity).all()

    def get_first_with_quantity_more(self, quantity: int) -> Order:
        return self._session.query(Order).filter(Order.quantity > quantity).first()

    def add_order(self, data:dict) -> None:
        order = Order(**data)
        self._session.add(order)
        self._session.commit()

    def change_quantity_for(self, id: str,  quantity: int) -> None:
        self._session.query(Order).filter(Order.id == id).update({"quantity": quantity})
