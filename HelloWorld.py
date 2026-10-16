message = "Hello World"
print(message)

name = input("Whats your name: ")
weight = float(input("In Kg: "))
cost = 12000

total = weight * cost

print("------------- RESULTS --------------")
print(f"Customer: {name}")
print(f"----- COST WEIGHT -----")
print(f" TOTAL ${total:,.2f}")
print("----------------------------------")
print("Thank you for your purchase")