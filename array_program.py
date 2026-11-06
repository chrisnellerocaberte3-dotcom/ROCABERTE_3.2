# Assessment 3.2 - ARRAY: Insert and Remove Letters
# Author: Rocaberte, Chrisnelle Mhae B. | BSIT 2F

letters = []  # Step 2: create an empty array


def insert_word():
    """Insert each letter of a word into the array."""
    word = input("Enter a word: ").upper()
    for ch in word:
        if ch.isalpha():
            letters.append(ch)
            print(f"Inserted {ch} -> {letters}")


def insert_letter():
    ch = input("Enter one letter: ").upper()
    if len(ch) == 1 and ch.isalpha():
        letters.append(ch)
        print(f"Inserted {ch} -> {letters}")
    else:
        print("Please enter exactly one letter.")


def remove_first():
    """Remove the first letter of the array."""
    if not letters:
        print("Array is empty. Nothing to remove.")
    else:
        removed = letters.pop(0)
        print(f"Removed {removed} -> {letters if letters else '[] - Empty'}")


def remove_all():
    """Remove the first letter repeatedly until the array is empty."""
    if not letters:
        print("Array is empty. Nothing to remove.")
    step = 1
    while letters:
        letters.pop(0)
        print(f"{step}. {letters if letters else '[] - Empty'}")
        step += 1


def display():
    print("Array:", letters if letters else "[] - Empty")


while True:
    print("\n===== ARRAY MENU =====")
    print("1. Insert a word (letter by letter)")
    print("2. Insert one letter")
    print("3. Display array")
    print("4. Remove first letter")
    print("5. Remove all (first letter repeatedly)")
    print("6. Exit")
    choice = input("Choose (1-6): ")

    if choice == "1":
        insert_word()
    elif choice == "2":
        insert_letter()
    elif choice == "3":
        display()
    elif choice == "4":
        remove_first()
    elif choice == "5":
        remove_all()
    elif choice == "6":
        print("Program ended.")
        break
    else:
        print("Invalid choice. Try again.")