print("Welcome to my grocery billing que program")
low_price_items=0
medium_price_items=0
high_price_items=0
customer_served=0
total_sales=0
billing=True
while billing:
    input("Enter your name please: ")
    item_count=int(input("Enter the amount of items you have: "))
    if item_count<=0:
        input("Please enter the amount of items you have: ")
    else:
        customer_total=0
        item_number=1
        while item_number<=item_count:
            name=input("Enter the item: ")
            price=int(input("Enter the item price: "))
            quantity=int(input("Enter the item quantity"))
            if quantity<=0:
                print("Enter an item quality above 0")
            else:
                item_total= price * quantity
                print("item name: ", name, ",item quantity: ", quantity, ",item price: ", item_total)
                customer_total+=item_total
            if price < 50:
                    low_price_items += quantity
            elif 50 <= price <= 100:
                    medium_price_items += quantity
            else:
                    high_price_items += quantity
                    item_number+=1
                    customer_served+=1
                    customer_total+=total_sales
                    print("Your total bill is:", total_sales)