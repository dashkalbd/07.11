class Book:
    def __init__(self, number, title, author, year):
        self.number = number
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"#{self.number} | {self.title} | {self.author} | {self.year}"


class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # 7. is the tree empty
    def is_empty(self):
        return self.root is None

    # 1. add a book
    def insert(self, book):
        if self.is_empty():
            self.root = Node(book)
            print("Book added")
        else:
            self._insert(self.root, book)

    def _insert(self, node, book):
        if book.number == node.book.number:
            print(f"Book with number {book.number} already exists")
        elif book.number < node.book.number:
            if node.left is None:
                node.left = Node(book)
                print("Book added")
            else:
                self._insert(node.left, book)
        else:
            if node.right is None:
                node.right = Node(book)
                print("Book added")
            else:
                self._insert(node.right, book)

    # 2. search by number
    def search(self, number):
        current = self.root
        while current is not None:
            if number == current.book.number:
                return current.book
            elif number < current.book.number:
                current = current.left
            else:
                current = current.right
        return None

    # 3. all books sorted by number
    def show_sorted(self, node):
        if node is None:
            return
        self.show_sorted(node.left)
        print(node.book)
        self.show_sorted(node.right)

    # 4. smallest number
    def find_min(self):
        if self.is_empty():
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current.book

    # 5. biggest number
    def find_max(self):
        if self.is_empty():
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current.book

    # 6. number of books
    def count(self, node):
        if node is None:
            return 0
        return 1 + self.count(node.left) + self.count(node.right)

    # 8. tree structure
    def show_structure(self, node, level=1, side="root"):
        if node is None:
            return
        print(f"Level {level} ({side}): {node.book}")
        self.show_structure(node.left, level + 1, f"left of {node.book.number}")
        self.show_structure(node.right, level + 1, f"right of {node.book.number}")


def menu():
    tree = BinarySearchTree()

    # a few books to start with
    tree.insert(Book(50, "Kobzar", "Taras Shevchenko", 1840))
    tree.insert(Book(30, "Tyhrolovy", "Ivan Bahrianyi", 1944))
    tree.insert(Book(70, "Lisova pisnia", "Lesia Ukrainka", 1911))
    tree.insert(Book(20, "Zakhar Berkut", "Ivan Franko", 1883))
    tree.insert(Book(40, "Kaidasheva simia", "Ivan Nechui-Levytskyi", 1879))

    while True:
        print()
        print("1 - Add book")
        print("2 - Find book by number")
        print("3 - Show all books (sorted)")
        print("4 - Book with smallest number")
        print("5 - Book with biggest number")
        print("6 - Number of books")
        print("7 - Is the tree empty?")
        print("8 - Show tree structure")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            number = int(input("Inventory number: "))
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            tree.insert(Book(number, title, author, year))

        elif choice == "2":
            number = int(input("Inventory number: "))
            book = tree.search(number)
            if book is None:
                print("Book not found")
            else:
                print(book)

        elif choice == "3":
            if tree.is_empty():
                print("Tree is empty")
            else:
                tree.show_sorted(tree.root)

        elif choice == "4":
            book = tree.find_min()
            if book is None:
                print("Tree is empty")
            else:
                print(book)

        elif choice == "5":
            book = tree.find_max()
            if book is None:
                print("Tree is empty")
            else:
                print(book)

        elif choice == "6":
            print("Number of books:", tree.count(tree.root))

        elif choice == "7":
            if tree.is_empty():
                print("Tree is empty")
            else:
                print("Tree is not empty")

        elif choice == "8":
            if tree.is_empty():
                print("Tree is empty")
            else:
                tree.show_structure(tree.root)

        elif choice == "0":
            print("Goodbye")
            break

        else:
            print("Wrong choice, try again")


menu()