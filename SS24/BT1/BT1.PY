class CoffeeOrder:

    vat_rate = 0.10

    def __init__(self, table_number):
        self.table_number = table_number
        self.__total_amount = 0

    def add_item(self, price):

        if price > 0:
            self.__total_amount += price

    @property
    def total_amount(self):
        return self.__total_amount

    def calculate_final_bill(self):

        vat_money = self.__total_amount * CoffeeOrder.vat_rate

        return self.__total_amount + vat_money

    @classmethod
    def update_vat_rate(cls, new_rate):

        if 0 <= new_rate <= 1:
            cls.vat_rate = new_rate

order_table1 = CoffeeOrder("Bàn 1")
order_table2 = CoffeeOrder("Bàn 2")

order_table1.add_item(50000)
order_table2.add_item(30000)

print("Tổng tiền bàn 1:", order_table1.total_amount)
print("Tổng tiền bàn 2:", order_table2.total_amount)

print("Cập nhật VAT xuống 8%")

CoffeeOrder.update_vat_rate(0.08)

print("VAT bàn 1:", order_table1.vat_rate)
print("VAT bàn 2:", order_table2.vat_rate)

print()

print(
    f"Tổng tiền Bàn 1 sau VAT: {order_table1.calculate_final_bill():,.0f} VNĐ"
)

print(
    f"Tổng tiền Bàn 2 sau VAT: {order_table2.calculate_final_bill():,.0f} VNĐ"
)