cart = []
def add_item(item):
    cart.append(item)
    print(item)
    print( f"{item} has ben  added")

def remove_item(item):
    try:
        cart.remove(item)
        print(item)
        print(f"{item} has been removed")
    except:
        print(cart)
        print('Sorry we could not remove that item')

def show_cart():
    if cart:
        print(cart)
        print("here is cart")
        for item in cart:
            print(f"{item}")
    else:
        print("Your cart is empty")

def clear_cart():
    cart.clear()
    print("Your chart has been cleared")

def main():
    done = False

    while not done:

        action = input("Choose action:add, delete, quit or show chart: ").lower()
        if action == "quit":
            print("Thanks for shopping with us")
            break
        elif action == "add":
            item = input("What would you like to add: ").title()
            add_item(item)
        elif action == "remove":
                item = input("What would you like to add: ").title()
                remove_item(item)
        elif action == "show":
                show_cart()
        elif action == "clear":
                clear_cart()
        else:
                print("Unrecognized Action")
main()
