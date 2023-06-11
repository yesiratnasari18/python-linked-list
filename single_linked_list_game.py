class item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None

    def add_item(self, name, importance):
        new_item = item(name, importance)

        if self.head is None:
            self.head = new_item
        elif new_item.importance < self.head.importance:
            new_item.next = self.head
            self.head = new_item
        else:
            current = self.head
            while current.next is not None and new_item.importance >= current.next.importance:
                current = current.next
            new_item.next = current.next
            current.next = new_item

    def remove_item(self, name):
        if self.head is None:
            return
            
        if self.head.name == name:
            self.head = self.head.next
            return
            
        current = self.head
        while current.next is not None and current.next.name != name:
            current = current.next

        if current.next is not None:
                current.next = current.next.next

    def print_items(self):
        if self.head is None:
            print("Tas Kosong.")
            return
                
        current = self.head
        print("Daftar item dalam tas:")
        while current is not None:
            print(f"Nama: {current.name} | Tingkat Kepentingan: {current.importance}")
            current = current.next


inventory = Inventory()

inventory.add_item("Potion", 3)
inventory.add_item("Key", 1)
inventory.add_item("Golden Coin", 2)

inventory.print_items()

inventory.remove_item("Key")

inventory.print_items()



