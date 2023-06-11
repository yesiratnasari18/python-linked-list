class product:
    def __init__(self, name, code, stock):
        self.code = code
        self.name = name
        self.stock = stock
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = product(name, code, stock)

        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next is not None :
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        if self.head is None:
            return
        
        if self.head.code == code:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None and current.next.code != code:
            current = current.next

        if current.next is not None:
            current.next = current.next.next

    def print_inventory(self):
        if self.head is None:
            print("Inventaris kosong.")
            return
        
        current = self.head
        print("Daftar Produk:")
        while current is not None:
            print(f"Nama: {current.name} | Kode: {current.code} | Stock: {current.stock}")
            current = current.next


inventory = Inventory()

inventory.add_product("Pensil", "P001", 15)
inventory.add_product("Pulpen", "P002", 25)
inventory.add_product("Buku", "B001", 10)

inventory.print_inventory()

inventory.remove_product("P002")

print('Update Produk')
inventory.print_inventory()

           
        