# As a Store Manager, I need a way to define Products and Laptops so I can track inventory.
# Task List:
# - Create class 'Product' with private attributes: __name, __sku, __price.
# - Create Mutators (Setters) and Accessors (Getters) for all three.
# - Create class 'Laptop' that inherits from 'Product'.
# - Add Laptop specific private attributes: __ram, __storage, __touchscreen.
# - Create method 'calculate_discount(percent)' that returns the reduced price.


class Product:
    def __init__(self, name, sku, price):
        self.__name = name  # Private attribute
        self.__sku = sku
        self.__price = price

    def get_name(self):  # Getter
        return self.__name
        return self.__sku
        return self.__price


class Laptop(Product):
    def __init__(self, name, ram, storage, touchscreen):
        super().__init__(name)  # Parent handles 'name'
        self.__ram = ram  # Child handles 'ram'
        self.__storage = storage
        self.__touchscreen = touchscreen

    def calculate_discount(percent):
        return percent


with open("sales.txt", "r") as f:
    for line in f:
        clean_line = line.strip()  # Removes invisible \n
