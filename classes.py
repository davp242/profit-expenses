# New file to try using classes and more OOP for orders, mostly expirementing and learning right now

# Creates "order" class
class orders:
    def __init__(self, name, price, address, order_date, shipping_date, tracking_number):
        self.name = name
        self.price = price
        self.address = address
        self.order_date = order_date
        self.shipping_date = shipping_date
        self.tracking_number = tracking_number

name = input("name")
price = float(input("price"))
add = input("add")
orddate = input("orddate")
shipdate = input("shipdate")
trackno = input("trackno")

order1 = orders(str(name),float(price),str(add),str(orddate),str(shipdate),str(trackno))

print("Below should be the price entry")
print(str(order1.price))

print("below should be the tracking number")
print(order1.tracking_number)

print("below should be the name")
print(order1.name)