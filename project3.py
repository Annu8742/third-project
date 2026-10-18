#Billing System (OOP-Based)
#Objective
#To develop a billing system using Object-Oriented Programming that stores product details,
# calculates the total price and tax, and displays the final bill in tabular format.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self, tax_rate=18):
        self.products = []
        self.tax_rate = tax_rate

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(product.get_total() for product in self.products)

    def calculate_tax(self):
        return self.calculate_total() * self.tax_rate / 100

    def display_bill(self):
        print("\n" + "=" * 65)
        print("                    CUSTOMER BILL")
        print("=" * 65)

        print(f"{'Product':<20}{'Price':>12}{'Quantity':>12}{'Total':>15}")
        print("-" * 65)

        for product in self.products:
            total = product.get_total()
            print(
                f"{product.name:<20}"
                f"{product.price:>12.2f}"
                f"{product.quantity:>12}"
                f"{total:>15.2f}"
            )

        print("-" * 65)

        subtotal = self.calculate_total()
        tax = self.calculate_tax()
        grand_total = subtotal + tax

        print(f"{'Subtotal:':>45} ₹{subtotal:>12.2f}")
        print(f"{'Tax (' + str(self.tax_rate) + '%):':>45} ₹{tax:>12.2f}")
        print(f"{'Grand Total:':>45} ₹{grand_total:>12.2f}")
        print("=" * 65)
        print("             Thank you for shopping!")


# Creating the bill
bill = Bill(tax_rate=18)

# Creating product objects
p1 = Product("Notebook", 50, 3)
p2 = Product("Pen", 10, 5)
p3 = Product("School Bag", 500, 1)

# Adding products to the bill
bill.add_product(p1)
bill.add_product(p2)
bill.add_product(p3)

# Displaying the final bill
bill.display_bill()