class Order:
    def __init__(self, client_name, room_type, days, price):
        self.__client_name = client_name
        self.__room_type = room_type
        self.__days = days
        self.__price = price

    def display_order(self):
        print("Client Name:", self.__client_name)
        print("Room Type:", self.__room_type)
        print("Days:", self.__days)
        print("Price:", self.__price)

    def change_room_type(self, new_room_type):
        self.__room_type = new_room_type
        print("Room type changed successfully.")

    def change_days(self, new_days):
        self.__days = new_days
        print("Number of days changed successfully.")

    def delete_order(self):
        self.__client_name = None
        self.__room_type = None
        self.__days = None
        self.__price = None
        print("Order deleted successfully.")




order = Order("John Doe", "Single", 5, 500)
order.display_order()
order.change_room_type("Double")
order.change_days(7)
order.display_order()
order.delete_order()
order.display_order()