class Supermarket:
    def __init__(self, location, name, product, customer):
        self.location = location
        self.name = name
        self.product = product
        self.customer = customer

    def print_location(self):
        print(f"위치: {self.location}")

    def change_category(self, new_product):
        self.product = new_product
        print(f"파는 물건 변경: {self.product}")

    def show_list(self):
        print(f"현재 파는 물건: {self.product}")

    def enter_customer(self):
        self.customer = self.customer + 1
        print(f"현재 고객 수: {self.customer}")

    def show_info(self):
        print(f"위치: {self.location}, 가게이름: {self.name}, 상품: {self.product}, 고객수: {self.customer}")

# 예시 사용
shop = Supermarket("마포구 염리동", "마켓온", "음료", 5)
shop.print_location()
shop.change_category("음료")
shop.show_list()
shop.enter_customer()
shop.show_info()
