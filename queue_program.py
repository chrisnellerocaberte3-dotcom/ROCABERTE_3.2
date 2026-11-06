# Assessment 3.2 - QUEUE (FIFO): Enqueue and Dequeue Letters
# Author: Rocaberte, Chrisnelle Mhae B. | BSIT 2F

from collections import deque

queue = deque()  # Step 2: empty queue (front = left, rear = right)


def enqueue(ch):
    queue.append(ch)  # add at the rear
    print(f"Enqueued {ch}")


def dequeue():
    """Remove the front letter (first one inserted)."""
    if not queue:
        print("Queue is empty (underflow). Nothing to dequeue.")
        return
    print(f"Dequeued {queue.popleft()}")


def front():
    if not queue:
        print("Queue is empty.")
    else:
        print(f"Front letter: {queue[0]}")


def display():
    if not queue:
        print("Queue: [] - Empty")
    else:
        print("Queue (front to rear):", list(queue))


while True:
    print("\n===== QUEUE (FIFO) MENU =====")
    print("1. Enqueue a word (letter by letter)")
    print("2. Enqueue one letter")
    print("3. Dequeue (remove front)")
    print("4. Show front")
    print("5. Display queue")
    print("6. Dequeue all")
    print("7. Exit")
    choice = input("Choose (1-7): ")

    if choice == "1":
        word = input("Enter a word: ").upper()
        for ch in word:
            if ch.isalpha():
                enqueue(ch)
        display()
    elif choice == "2":
        ch = input("Enter one letter: ").upper()
        if len(ch) == 1 and ch.isalpha():
            enqueue(ch)
        else:
            print("Please enter exactly one letter.")
    elif choice == "3":
        dequeue()
    elif choice == "4":
        front()
    elif choice == "5":
        display()
    elif choice == "6":
        if not queue:
            print("Queue is empty (underflow). Nothing to dequeue.")
        step = 1
        while queue:
            print(f"{step}. Remove {queue.popleft()}")
            step += 1
        display()
    elif choice == "7":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")