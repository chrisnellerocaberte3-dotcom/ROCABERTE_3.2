# Assessment 3.2 - STACK (LIFO): Push and Pop Letters
# Author: Rocaberte, Chrisnelle Mhae B. | BSIT 2F

stack = []  # Step 2: empty stack (top = end of the list)


def push(ch):
    stack.append(ch)
    print(f"Pushed {ch}")


def pop():
    """Remove the top letter (last one pushed)."""
    if not stack:
        print("Stack is empty (underflow). Nothing to pop.")
        return
    print(f"Popped {stack.pop()}")


def peek():
    if not stack:
        print("Stack is empty.")
    else:
        print(f"Top letter: {stack[-1]}")


def display():
    if not stack:
        print("Stack: [] - Empty")
    else:
        print("Stack (bottom to top):", stack)
        print("Top of stack:", stack[-1])


while True:
    print("\n===== STACK (LIFO) MENU =====")
    print("1. Push a word (letter by letter)")
    print("2. Push one letter")
    print("3. Pop (remove top)")
    print("4. Peek (see top)")
    print("5. Display stack")
    print("6. Pop all")
    print("7. Exit")
    choice = input("Choose (1-7): ")

    if choice == "1":
        word = input("Enter a word: ").upper()
        for ch in word:
            if ch.isalpha():
                push(ch)
        display()
    elif choice == "2":
        ch = input("Enter one letter: ").upper()
        if len(ch) == 1 and ch.isalpha():
            push(ch)
        else:
            print("Please enter exactly one letter.")
    elif choice == "3":
        pop()
    elif choice == "4":
        peek()
    elif choice == "5":
        display()
    elif choice == "6":
        if not stack:
            print("Stack is empty (underflow). Nothing to pop.")
        step = 1
        while stack:
            print(f"{step}. Remove {stack.pop()}")
            step += 1
        display()
    elif choice == "7":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")