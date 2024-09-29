class Inventory:
    def __init__(self):
    
        self.items = {}

    def add_item(self, item_name, quantity):
        # Confirm if the item is available , update quantity if it does
        if item_name in self.items:
            self.items[item_name] += quantity
            print(f"Updated {item_name}: New quantity = {self.items[item_name]}")
        else:
            self.items[item_name] = quantity
            print(f"Added {item_name}: Quantity = {self.items[item_name]}")

    def get_item(self, item_name):
        # Retrieve specific item from inventory
        if item_name in self.inventory:
            print(f"{item_name}: Quantity = {self.items[item_name]}")
        else:
            print(f"{item_name} not found.")

    def total_inventory(self):
        #  total quantity of all the items
        total = sum(self.items.values())
        print(f"Total quantity of all items: {total}")

# Main function
def main():
    inventory = Inventory()

    while True:
        print("\nInventory Menu:")
        print("1. Add/Update Item")
        print("2. Get Item details")
        print("3. Total Quantity")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory.add_item(item_name, quantity)
        elif choice == '2':
            item_name = input("Enter item name to retrieve: ")
            inventory.get_item(item_name)
        elif choice == '3':
            inventory.total_inventory()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
