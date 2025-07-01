#Define the menu of restaurant 
menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
}

#greet
print("Welcome to SK Restaurant")
print("Pizza: Rs40\npasta: Rs50\nburger:Rs60\nsalad:Rs70\ncoffee:Rs80")

order_total = 0
#80+70=150
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1] #0+50
    print(f"Your item '{item_1}' has been added to your order.")

else:
   print(f"Ordered item '{item_1}' is not available yet.")
another_order = input("Do you want to add another item? (Yes/No): ")
if another_order.strip().lower() == "yes":
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
       print(f"Ordered item '{item_2}' is not available!")
if another_order.strip().lower() == "yes":
    item_3 = input("Enter the name of third item =")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Item '{item_3}' has been added to your order.")
    else:
       print(f"Ordered item '{item_3}' is not available!")
if another_order.strip().lower() == "yes":
    item_4= input("Enter the name of fourth item =")
    if item_4 in menu:
        order_total += menu[item_4]
        print(f"Item '{item_4}' has been added to your order.")
    else:
       print(f"Ordered item '{item_4}' is not available!")


print(f"The total amount of items to pay is {order_total}")            



