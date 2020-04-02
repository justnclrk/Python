# Assignment: Product
# The owner of a store wants a program to track products. Create a product class to fill the following requirements.
class Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
    def sell(self):
        self.status = 'sold'
        return self
    def add_tax(self, decimal):
        self.price += round(self.price * decimal, 2)
        return self
    def return_item(self, return_state):
        if return_state == 'defective':
            self.status = 'defective'
            self.price = 0
        if return_state  == 'new in box':
            self.status = 'for sale'
        if return_state == 'opened box':
            self.status = 'used'
            self.price = self.price * .8
        return self.display_info()
    def display_info(self):
        print 'Price: ${}'.format(self.price)
        print 'Item_name: {}'.format(self.item_name)
        print 'Weight: {} lbs'.format(self.weight)
        print 'Brand: {}'.format(self.brand)
        print 'status: {}'.format(self.status)
        return self
car = Product(20000, 'Civic', '1500', 'Honda', '')
phone = Product(600, 'Pixel 2', '3', 'Google', '')
apple = Product(10, 'Apple', '.05', 'Granny Smith', '')
car.add_tax(.08).display_info().sell().display_info().return_item('opened')
print '----------'
phone.add_tax(.093).display_info().sell().display_info().return_item('new in box')
print '----------'
apple.add_tax(.093).display_info().sell().display_info().return_item('defective')