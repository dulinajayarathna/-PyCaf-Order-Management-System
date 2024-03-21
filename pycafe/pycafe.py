from typing import List, Dict, Any


def add_order(order_id, item_name, quantity=1):
    order_details = {
        'order_id': order_id,
        'item_name': item_name,
        'quantity': quantity
    }
    print(f"Order {order_id} for {quantity} {item_name}(s) has been added.")
    return order_details


def print_orders(orders):
    print("Current Orders:")
    for order in orders:
        print(f"Order ID: ['order_id'], Item:['item_name'], Quantity:['quantity']")


def main(orders=[]):
    orders.append(add_order(1, "Latte"))
    orders.append(add_order(2, "Cheese cake"))
    orders.append(add_order(3, "Veggie Sandwich"))

    print_orders(orders)


if __name__ == "__main__":
    main()
