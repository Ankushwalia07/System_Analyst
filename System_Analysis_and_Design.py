class Product:
    def __init__(self, name, sku, price, quantity):
        self.name = name
        self.sku = sku
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.products = [] #Enter the Procducts here

    def add_product(self, name, sku, price, quantity):
        product = Product(name, sku, price, quantity)
        self.products.append(product)

    def update_quantity(self, sku, new_quantity):
        for product in self.products:
            if product.sku == sku:
                product.quantity = new_quantity
                break

    def get_low_stock_items(self, threshold):
        return [product for product in self.products if product.quantity <= threshold]

    def generate_report(self):
        print("Product Report:")
        for product in self.products:
            print(f"Name: {product.name}, SKU: {product.sku}, Price: {product.price}, Quantity: {product.quantity}")

# def main():
#     inventory = Inventory()
#
#     while True:
#         print("1. Add Product")
#         print("2. Update Quantity")
#         print("3. Get Low Stock Items")
#         print("4. Generate Report")
#         print("5. Exit")
#         choice = int(input("Enter your choice: "))
#
#         if choice == 1:
#             name = input("Enter product name: ")
#             sku = input("Enter SKU: ")
#             price = float(input("Enter price: "))
#             quantity = int(input("Enter quantity: "))
#             inventory.add_product(name, sku, price, quantity)
#             print("Product added successfully!")
#
#         elif choice == 2:
#             sku = input("Enter SKU of the product to update quantity: ")
#             new_quantity = int(input("Enter new quantity: "))
#             inventory.update_quantity(sku, new_quantity)
#             print("Quantity updated successfully!")
#
#         elif choice == 3:
#             threshold = int(input("Enter the threshold quantity for low stock items: "))
#             low_stock_items = inventory.get_low_stock_items(threshold)
#             print("Low Stock Items:")
#             for item in low_stock_items:
#                 print(f"Name: {item.name}, SKU: {item.sku}, Quantity: {item.quantity}")
#
#         elif choice == 4:
#             inventory.generate_report()
#
#         elif choice == 5:
#             print("Exiting the system.")
#             break
#
#         else:
#             print("Invalid choice. Please try again.")
#
# if __name__ == "__main__":
#     main()
