# This is the parent Product. The general humankind. The cloth at which you cut.
class Product:
    def __init__(self, name, sku, price):
        self.__name = name  # Priv Att
        self.__sku = sku
        self.__price = price

    def get_name(self):  # Getters:
        return self.__name

    def get_sku(self):
        return self.__sku

    def get_price(self):
        return self.__price

    def calculate_discount_price(self, discount):
        return self.__price * (1 - discount)


# This is the child. The Mexican to the human. The cut at which was once the cloth.
class Laptop(Product):
    def __init__(self, name, sku, price, ram, storage, touchscreen, discount):
        super().__init__(name, sku, price)  # Parent handles 'name'
        self.__ram = ram  # Child handles 'ram', 'storage', 'touchscreen' because notice the parent Product does not include these
        self.__storage = storage
        self.__touchscreen = touchscreen
        self.__discount = discount

    # Im actually not sure if this was calculated correctly so bear with me
    def calculate_discount_price(self, discount):
        base_price = self.get_price()  # Refering to line 14
        return base_price * (
            1 - (discount / 100)
        )  # Actually applying the discount part.

    # Idk why it broke like that when I saved but I don't like it. Whatever.


# As a User, I want to type in laptop details and see a formatted spec sheet. Because why would a user make it easy on me.
# Wtf does it mean Import products module?

name = input(
    "\nUser, I need a couple things if Im gonna make this spec sheet. Gimmie a name: "
).strip()
sku = input("\nAlright, now I need the SKU: ").strip()
ram = input("\nThe RAM? ").strip()
price = float(input("\nHow much does it cost? Gimmie the price: ").strip())
storage = input("\nWhat't the storage? ").strip()
touchscreen = input("\nTouchscreen? (yes/no): ")

user_laptop = Laptop(name, sku, price, ram, storage, touchscreen, 0)
# Okay now that iv'e got a hold of the users I.P adress and mothers maiden name, we can finally instantiate.

print("\n--- SPEC SHEET ---")
print(f"Device: {user_laptop.get_name()}")
if touchscreen.lower() == "yes":
    print("Is touchscreen")
else:
    pass

print(f"Price: ${user_laptop.get_price()}")
print(
    f"Discounted Price (15% off): ${user_laptop.calculate_discount_price(15):.2f}"
)  # .2f in case it would come out as a hideous decimal
