class Order:
    def __init__(self, client_name, address, car_type, price):
        self.__client_name = client_name
        self.__address = address
        self.__car_type = car_type
        self.__price = price

    def display_order(self):
        print("Client Name:", self.__client_name)
        print("Address:", self.__address)
        print("Car Type:", self.__car_type)
        print("Price:", self.__price)

    def change_address(self, new_address):
        self.__address = new_address
        print("Address changed successfully.")

    def change_car_type(self, new_car_type):
        self.__car_type = new_car_type
        print("Car type changed successfully.")

    def delete_order(self):
        self.__client_name = None
        self.__address = None
        self.__car_type = None
        self.__price = None
        print("Order deleted successfully.")




order = Order("John Doe", "123 Main St", "Sedan", 25)
order.display_order()
order.change_address("456 Elm St")
order.change_car_type("SUV")
order.display_order()
order.delete_order()
order.display_order()