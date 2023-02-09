from tabulate import tabulate

class Transaction:
    def __init__(self):
        """Ini merupakan fungsi untuk menginisialisasi dictionary data items yang akan diinput oleh user."""
        self.total_cost = 0
        self.items = {}

    def add_item(self, item, quantity, cost):
        """
        fungsi menambahkan barang/item

        parameters
        item        : str   nama item
        quantity    : int   jumlah item
        cost        : float harga item
        """
        self.items[item] = (cost,quantity)
        self.total_cost += cost*quantity

    def delete_item(self, item):
        """Ini merupakan fungsi untuk menghapus barang per item."""
        cost, quantity = self.items.pop(item)
        self.total_cost -= cost*quantity

    def update_item_all(self, item, new_item, new_quantity, new_cost):
        """Ini merupakan fungsi test awal untuk mengupdate, tp bisanya berbarengan bukan terpisah."""
        cost, quantity = self.items[item]
        self.total_cost -= cost*quantity
        self.items[new_item] = (new_cost,new_quantity)
        self.total_cost += new_cost*new_quantity

    def update_item(self, item_name, new_item_cost=None, new_item_quantity=None):
        """Ini merupakan fungsi untuk mengupdate nama barang."""
        try:
            item_cost, item_quantity = self.items[item_name]
            if new_item_cost is not None:
                self.update_item_cost(item_name, new_item_cost)
            if new_item_quantity is not None:
                self.update_item_quantity(item_name, new_item_quantity)
        except KeyError:
            print(f"Item {item_name} not found.")

    def update_item_cost(self, item_name, new_item_cost):
        """Ini merupakan fungsi untuk mengupdate harga barang."""
        try:
            item_cost, item_quantity = self.items[item_name]
            self.total_cost -= item_cost * item_quantity
            self.items[item_name][0] = new_item_cost
            self.total_cost += new_item_cost * item_quantity
        except KeyError:
            print(f"Item {item_name} not found.")

    def update_item_quantity(self, item_name, new_item_quantity):
        """Ini merupakan fungsi untuk mengupdate jumlah barang."""
        try:
            item_cost, item_quantity = self.items[item_name]
            self.total_cost -= item_cost * item_quantity
            self.items[item_name][1] = new_item_quantity
            self.total_cost += item_cost * new_item_quantity
        except KeyError:
            print(f"Item {item_name} not found.")

    def reset_transaction(self):
        """Ini merupakan fungsi untuk menghapus semua barang yang diinput."""
        self.items.clear()
        self.total_cost = 0

    def total_price(self):
        """
        Ini merupakan fungsi untuk menghitung harga barang yang diinput sebelumnya.

        Ada total harga barang yang kena perhitungan diskon,
        bila total nya melebihi jumlah tertentu

        final_price = total harga yang sudah termasuk diskon
        total_cost = total harga yang tidak terkena diskon
        """
        if self.total_cost > 200_000:
            discount = self.total_cost * 0.05
            final_price = self.total_cost - discount
            return final_price
        elif self.total_cost > 300_000:
                discount = self.total_cost * 0.08
                final_price = self.total_cost - discount
                return final_price
        elif self.total_cost > 500_000:
                discount = self.total_cost * 0.1
                final_price = self.total_cost - discount
                return final_price
        else:
            return self.total_cost

    def check_order(self):
        """
        Ini merupakan fungsi untuk mengecheck semua barang yang diinput sebelumnya.

        Menggunakan tabulate untuk menampilkan datanya

        diimport dulu di atas tabulate nya
        """
        print(f"Pemesanan sudah benar\n")
        headers = ["Nama Item", "Harga Item", "Jumlah Item", "Total Harga"]
        data = []
        for item, (cost, quantity) in self.items.items():
            data.append([item, cost, quantity, cost * quantity])
        print(tabulate(data, headers, tablefmt="github"))

    def print_receipt(self):
        """Ini merupakan fungsi untuk print pada function check_order."""
        self.check_order()

    def print_item(self):
        """Ini merupakan fungsi untuk print data item yang dibelanjakan dan total harga yg harus dibayarkan."""
        print(f"Receipt:")
        for item, (cost,quantity) in self.items.items():
            print(f'Item yang dibeli adalah {item} : [{quantity}, {cost}]')
        print(f"Total belanja yang harus dibayarkan adalah Rp. " + str(self.total_price()))

trans_123 = Transaction()
while True:
    print('|=====', 'Sistem Kasir', '=====|')
    print('- ketik "cek" untuk melihat barang yang di order -')
    print('- ketik "done" untuk exit dari sistem kasir -')
    print('- ketik "delete" untuk menghapus 1 barang yang di order -')
    print('- ketik "delete all" untuk menghapus semua barang yang di order -')
    print('- ketik "update" untuk mengupdate item barang yang di order -')
    print('- ketik "update nama" untuk mengupdate nama barang yang di order -')
    print('- ketik "update jumlah" untuk mengupdate jumlah barang yang di order -')
    print('- ketik "update harga" untuk mengupdate harga barang yang di order -')
    print('|========================|\n')
    item = input(f'Masukkan nama barang yang ingin dibeli: ')
    if item.lower() == "done":
        break
    elif item.lower() == "cek":
        trans_123.print_receipt()
    elif item.lower() == "delete":
        item = input(f'Masukkan nama barang yang ingin di hapus: ')
        if item in trans_123.items:
            trans_123.delete_item(item)
        else:
            print(f'Barang yang mau di hapus tidak ada di dalam transaksi!')
    elif item.lower() == "delete all":
            print(f'Semua item berhasil di delete!')
            trans_123.reset_transaction()
    elif item.lower() == "update":
        item = input(f'Masukkan barang yang mau di update: ')
        if item in trans_123.items:
            new_item = input(f'Masukkan nama barang yang baru: ')
            new_quantity = int(input(f'Masukkan jumlah barang yang baru: '))
            new_cost = float(input(f'Masukkan harga barang yang baru: '))
            trans_123.update_item_all(item, new_item, new_quantity, new_cost)
        else:
            print(f'Barang yang mau di update tidak ditemukan pada transaksi!')
    else:
        quantity = float(input(f'Masukkan jumlah barang yang ingin dibeli: '))
        cost = float(input(f'Masukkan harga barang yang ingin dibeli: '))
        trans_123.add_item(item, quantity, cost)

trans_123.print_item()