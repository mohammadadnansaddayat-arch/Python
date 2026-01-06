TAX_RATE = 0.10

menu = {

"c-Burger": 500.00,
"veg-burger": 300.00,
"Burger": 300.00,
"c-Fries": 100.00,
"Fries": 50.00,
"c-Soup": 200.00,
"c-taco": 50.00,
"veg-taco": 30.00,
"Soda": 60.00,
"Salad": 120.00,
"Coke": 50.00,
"Pizza": 1020.00,
"Ice Cream": 30.00,
"Coffee": 20.00,
"Tea": 25.00,
"Juice": 30.00,
"Pasta": 150.00,
"Sandwich": 50.00,
"egg-sandwich":20.00,
"Water": 00.00

}

order = {}

def show_menu():
    print("\nMENU:")
    for item,price in menu.items():
        print(f"{item}: Rs. {price}")

def take_order():
    while True:
        item = input("\nEnter the item name you want to order(or type 'done' to finish): ").strip()
        if item.lower()== "done":
            break
        if item in menu:
            quanity = int(input(f"Enter the quanity for the {item}: "))
            if item in order:
                order[item] += quanity
            else:
                order[item] = quanity
        else:
            print("Item not found in the menu.Please try again...")

def calculate_total():
    total = 0.00
    for item,quanity in order.items():
        total += menu[item] * quanity
    tax = total * TAX_RATE 
    total_with_tax = total + tax
    return tax,total,total_with_tax

def print_bill():
    print("\n------Bill Summary-----")
    total, tax, total_with_tax = calculate_total()
    for item, quanaty in order.items():
        print(f"{item} x {quanaty} = Rs. {menu[item] * quanaty:.2f}")
    print(f"Subtotal: Rs. {total :.2f}")
    print(f"Tax:(10%): Rs. {tax:.2f}")
    print(f"total Amount: Rs. {total_with_tax:.2f}")

if __name__ == "__main__":
    show_menu()
    take_order()
    print_bill()
    print(f"\nHAVE A NICE DAY...")