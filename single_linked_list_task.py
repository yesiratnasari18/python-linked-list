class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None

class BudiList:
    def __init__(self):
        self.head = None

    def add_task (self, description, priority):
        new_task = Task(description, priority)

        if self.head is None:
            self.head = new_task
        elif new_task.priority < self.head.priority:
            new_task.next
            new_task.next = self.head
            self.head = new_task
        else:
            current = self.head
            while current.next is not None and new_task.priority >= current.next.priority:
                current = current.next
            new_task.next = current.next
            current.next = new_task

    def remove_task(self, description):
        if self.head is None:
            return

        if self.head.description == description:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None and current.next.description != description:
            current = current.next

        if current.next is not None:
            current.next = current.next.next

    def print_tasks(self):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        current = self.head
        print("Daftar tugas Budi:")
        while current is not None:
            print(f"Deskripsi: {current.description} | Prioritas: {current.priority}")
            current = current.next


task_list = BudiList()

task_list.add_task("Belajar anatomi tubuh manusia", 3)
task_list.add_task("Belajar Bahasa Inggris", 2)
task_list.add_task("Membaca Buku pengetahuan", 1)

print('List tugas awal')
task_list.print_tasks()

print('List Tugas Selanjutnya')
task_list.remove_task("Belajar Bahasa Inggris")

task_list.print_tasks()

