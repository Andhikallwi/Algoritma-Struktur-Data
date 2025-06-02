class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def search(self, target):
        current = self.head
        index = 0
        indices = []
        while current:
            if current.data == target:
                indices.append(index)
            current = current.next
            index += 1
        return indices

# Contoh penggunaan
linked_list = LinkedList()
data_mahasiswa = ["Jakarta", "Bandung", "Klaten", "Surabaya", "Klaten", "Medan", "Klaten", "Yogyakarta"]
for data in data_mahasiswa:
    linked_list.append(data)

# Mencari mahasiswa dari Klaten
indeks_klaten = linked_list.search("Klaten")
print(f"Mahasiswa dari Klaten berada di indeks: {indeks_klaten}")