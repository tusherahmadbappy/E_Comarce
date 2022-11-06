class Shoper:
    def __init__(self, name):
        self.name=name
        self.cart = []
    
    def add_to_cart(self, item, price, quantity):
        self.cart.append({'item':item, 'price':price, 'quantity':quantity})

    def checkout(self, amount):
        Total_Price = 0
        for item in self.cart:
            print(item)
            Total_Price += item['price'] * item['quantity']
        if amount < Total_Price:
            return f'Please give me more money {float(Total_Price - amount)} BD.TK'
        elif amount > Total_Price:
            return f'Here are the Item and Extra money {float(amount - Total_Price)} BD.TK'
        else:
            return 'Here are the item.'


shopping = Shoper('Tusher')
shopping.add_to_cart('Shirt',1800,2)
shopping.add_to_cart('Pant',2860,2)
shopping.add_to_cart('T-Shirt',1190,2)
shopping.add_to_cart('T-Shirt',750,3)

reply = shopping.checkout(14000)
print(reply)


    