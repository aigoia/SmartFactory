class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity = self.quantity + amount
        print(f"{self.name} 재고가 {amount}만큼 {'증가' if amount > 0 else '감소'}합니다. 현재 재고: {self.quantity}")    
    
    def display_info(self):
        print(f"상품명: {self.name}")
        print(f"가격: {self.price}원")
        print(f"재고: {self.quantity}개")
        
class Electronic(Product):
    def __init__(self, name, price, quantity, warranty_period=12):
        Product.__init__(self, name, price, quantity)
        self.warranty_period = warranty_period
    
    def extend_warranty_period(self, months):
        self.warranty_period = self.warranty_period + months
    
    def display_info(self):
        super().display_info()
        print(f"보증 기간: {self.warranty_period}개월")

class Food(Product):
    def __init__(self, name, price, quantity, expiration_data):
        Product.__init__(self, name, price, quantity)
        self.expiration_data = expiration_data
    
    def is_expired(self, current_date):
        return True if self.expiration_data[0] < current_date[0] else True \
            if self.expiration_data[1] < current_date[1] else True \
            if self.expiration_data[2] < current_date[2] else False
    
    def display_info(self, current_date=None):
        super().display_info()
        print(f"유통 기한: {self.expiration_data}개월")
        if None != current_date:
            return print("유통 기간이 넘었다.") if self.is_expired(current_date) else print("먹어도 괞찬다")

apple_keyboad = Electronic("Apple Keypad", 50000, 12, 24)
apple_keyboad.display_info()
print("")

apple = Food("Apple", 10000, 6, [2025, 10, 21])
apple.display_info([2015, 9, 21])
