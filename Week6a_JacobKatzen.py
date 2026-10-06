order = {"drink": "Latte", "size": "Large", "price": 5.50, "quantity": 2}
print(order["drink"])
print(order["price"])



print("\n")
for key in order.keys():
    print(key)

print("\n")
for value in order.values():
    print(value)

print("\n")
for key in order.keys():
    print(f"{key}: {order[key]}")

order["drink"] = "Coffee"
print(order["drink"])

order["size"] = "medium"
print(order["size"])

order["whipped cream"] = "yes"
print(order["whipped cream"])

order["flavor"] = "vanilla"
print(order["flavor"])

# you will get a syntax error because that value does not exist
# using the .get() method you will not get a value you will just get an empty value

order["flavor"] = "caramel"
order["quantity"] = 3

order["pickup"] = "10:30"

print("\n")
for key in order.keys():
    print(f"{key}: {order[key]}")