class Cart():

    def __init__(self, cart_1 = []):
        self.cart_1 = cart_1

    def add_item(self, item):
        self.item = item
        self.cart_1.append(self.item)
        print(self.cart_1)
        print(f"{self.item} has been added to your shopping cart")

    def remove_item(self, item):
        self.item = item
        self.cart_1.remove(self.item)
        try:
            print(self.cart_1)
            print(f"{self.item} has been removed from your shopping cart")

        except:
            print(self.cart_1)
            print('Sorry we could not remove that item')

    def show_cart(self):
        print(self.cart_1)

    def clear_cart(self):
        self.cart_1.clear()
        print("Your chart has been cleared")

    def main(self,):
        while True:
            action = input("Choose action:add, delete, quit, clear show chart: ").lower()
            if action.lower() == "quit":
                print("Thanks for shopping with us")
                break
            elif action.lower() == "add":
                self.item = input("What would you like to add: ").title()
                self.cart_1.append(self.item)
                print(self.cart_1)
                print(f"{self.item} has been added to your shopping cart")
            elif action.lower() == "remove":
                if self.item in self.cart_1:
                    self.item = input("What would you like to add: ").title()
                    self.cart_1.remove(self.item)
                    print(self.cart_1)
                    print(f"{self.item} has been removed from your shopping cart")
                else:
                    print(self.cart_1)
                    print('Sorry item is not present in cart')
            elif action.lower() == "show":
                print(self.cart_1)
            elif action.lower() == "clear":
                self.cart_1.clear()
                print(self.cart_1)
                print("Your chart has been cleared")
            else:
                print("Unrecognized Action")
        return

cart_2 = Cart()
cart_2.main()