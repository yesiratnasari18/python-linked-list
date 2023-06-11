class participant:
    def __init__(self, name, ranking):
        self.name = name
        self.ranking= ranking
        self.next = None

class Tournament:
    def __init__(self):
        self.head = None

    def add_participant(self, name, ranking):
        new_participant = participant(name, ranking)

        if self.head is None: 
            self.head = new_participant
        elif new_participant.ranking < self.head.ranking:
            new_participant.next = self.head
            self.head = new_participant
        else:
            current = self.head
            while current.next is not None and new_participant.ranking >= current.next.ranking:
                current = current.next
            new_participant.next = current.next
            current.next = new_participant

    def remove_participant(self, name):
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

    def print_participants(self):
        if self.head is None:
            print("Belum ada peserta terdaftar.")
            return

        current = self.head
        print("Daftar Peserta:")
        while current is not None:
            print(f"Nama: {current.name} | Peringkat: {current.ranking}")
            current = current.next


tournament = Tournament()

tournament.add_participant("Yesi", 1200)
tournament.add_participant("Ratna", 1500)
tournament.add_participant("Sari", 1000)

print('Hasil Pertandingan Awal')
tournament.print_participants()

tournament.remove_participant("Sari")
print('Pertandingan Selanjutnya')
tournament.print_participants()