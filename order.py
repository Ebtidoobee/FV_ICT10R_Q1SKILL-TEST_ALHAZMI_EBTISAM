from pyscript import document

def create_order(event=None):
# --- Customer Details ---
name = document.querySelector("#name").value
address = document.querySelector("#address").value
number = document.querySelector("#number").value

```
# --- Menu Items ---
checkboxes = document.querySelectorAll("input[name='items']:checked")

items = []
total = 0

# Loop through selected items
for checkbox in checkboxes:
    label = checkbox.parentElement.innerText.split("(")[0].strip()  # item name
    price = int(checkbox.value)  # numeric price
    items.append(f"{label} - ₱{price}")
    total += price

# If no items are selected
items_str = "\n".join(items) if items else "No items selected"

# --- Final Order Summary ---
order = f"""
```

👤 Customer Details:
Name     : {name}
Address  : {address}
Phone Number : {number}

🛒 Items Ordered:
{items_str}

💵 Total: ₱{total}
"""

```
# Show only once in #output
document.querySelector("#output").innerText = order
```
