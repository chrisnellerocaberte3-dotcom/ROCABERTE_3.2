# Assessment 3.2 - LINKED LIST: Insert and Delete Nodes
# Author: Rocaberte, Chrisnelle Mhae B. | BSIT 2F


class Node:
    def __init__(self, data):
        self.data = data   # the letter stored in this node
        self.next = None   # link to the next node


class LinkedList:
    def __init__(self):
        self.head = None   # Step 2: empty linked list

    def insert_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def delete_first(self):
        """Delete the first node (the head)."""
        if self.head is None:
            print("Linked list is empty. Nothing to delete.")
            return None
        removed = self.head.data
        self.head = self.head.next
        return removed

    def to_string(self):
        if self.head is None:
            return "HEAD -> NULL (Empty)"
        parts = []
        current = self.head
        while current is not None:
            parts.append(current.data)
            current = current.next
        return "HEAD -> " + " -> ".join(parts) + " -> NULL"


ll = LinkedList()

while True:
    print("\n===== LINKED LIST MENU =====")
    print("1. Insert a word (one node per letter)")
    print("2. Insert one letter at the end")
    print("3. Display linked list")
    print("4. Delete first node")
    print("5. Delete all (first node repeatedly)")
    print("6. Exit")
    choice = input("Choose (1-6): ")

    if choice == "1":
        word = input("Enter a word: ").upper()
        for ch in word:
            if ch.isalpha():
                ll.insert_end(ch)
                print(ll.to_string())
    elif choice == "2":
        ch = input("Enter one letter: ").upper()
        if len(ch) == 1 and ch.isalpha():
            ll.insert_end(ch)
            print(ll.to_string())
        else:
            print("Please enter exactly one letter.")
    elif choice == "3":
        print(ll.to_string())
    elif choice == "4":
        removed = ll.delete_first()
        if removed is not None:
            print(f"Deleted {removed}")
            print(ll.to_string())
    elif choice == "5":
        if ll.head is None:
            print("Linked list is empty. Nothing to delete.")
        step = 1
        while ll.head is not None:
            ll.delete_first()
            print(f"{step}. {ll.to_string()}")
            step += 1
    elif choice == "6":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")