TAX_RATE = 0.10

menu = {

"Burger": 123.00,
"Fries": 112.00,
"Soda": 60.00,
"Salad": 120.00,
"Coke": 50.00,
"Pizza": 500.00,
"Ice Cream": 150.00,
"Coffee": 200.00,
"Tea": 55.00,
"Juice": 90.00,
"Pasta": 250.00,
"Sandwich": 200.00,
"Water": 20.00

}

order = {}

def show_menu():
    print("\nMENU:")
    for item,price in menu.items():
        print(f"{item}: Rs. {price}")

def take_order():
    while True:
        item = input("\nEnter the item name you want to order(or type 'done' to finish)").strip()
        if item .lower()