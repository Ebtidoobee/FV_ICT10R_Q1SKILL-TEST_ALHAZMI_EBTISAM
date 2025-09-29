from pyscript import document


prices = {
    "Pasta": 100,
    "Croissant": 80,
    "Burger": 95,
    "Pie": 120
}

def generate_message(event):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    number = document.getElementById("number").value

   
    ordered_items = []
    total = 0

    for food_id, food_name in {
        "food1": "Pasta",
        "food2": "Croissant",
        "food3": "Burger",
        "food4": "Pie"
    }.items():
        checkbox = document.getElementById(food_id)
        if checkbox.checked:
            ordered_items.append(food_name)
            total += prices[food_name]

    
    if ordered_items:
        items_str = "\n".join(ordered_items)
    else:
        items_str = "No items selected."

    message = f"""
Order for: {name}
Address: {address}
Contact Number: {number}

Items Ordered:
{items_str}

Total: ₱{total}.00
"""

   
    output = document.getElementById("final")
    output.innerHTML = f"<pre>{message}</pre>"
