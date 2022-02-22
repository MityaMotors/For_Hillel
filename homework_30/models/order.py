from sqlalchemy import VARCHAR, Column, Integer
from ..core.base_model import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(VARCHAR(8), primary_key=True)
    product_id = Column(VARCHAR(10))
    quantity = Column(Integer)

    def __str__(self) -> str:
        return f"{self.id} | {self.product_id} | {self.quantity}"