# Assessment 3.2 - MAIN MENU
# Author: Rocaberte, Chrisnelle Mhae B. | BSIT 2F
# Run this file to choose which linear data structure program to open.
# Keep main.py in the same folder as the four program files.

import os
import runpy

FOLDER = os.path.dirname(os.path.abspath(__file__))

PROGRAMS = {
    "1": ("Array", "array_program.py"),
    "2": ("Linked List", "linked_list_program.py"),
    "3": ("Stack (LIFO)", "stack_program.py"),
    "4": ("Queue (FIFO)", "queue_program.py"),
}


def main():
    while True:
        print("\n===== LINEAR DATA STRUCTURE =====")
        for key, (name, _) in PROGRAMS.items():
            print(f"{key}. {name}")
        print("5. Exit")
        choice = input("Choose (1-5): ")

        if choice in PROGRAMS:
            name, filename = PROGRAMS[choice]
            print(f"\nOpening {name} program...")
            runpy.run_path(os.path.join(FOLDER, filename))
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()