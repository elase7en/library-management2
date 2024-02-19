books_info = [
    "İçimizdeki Şeytan,Sabahattin Ali,2019,250",
    "Suç ve Ceza,Fyodor Dostoyevski,1866,671",
    "1984,George Orwell,1949,328",
    "Harry Potter ve Felsefe Taşı,J.K. Rowling,1997,309",
    "Yabancı,Albert Camus,1942,185",
    "Simyacı,Paulo Coelho,1988,163",
    "Sefiller,Victor Hugo,1862,1232",
    "Don Kişot,Miguel de Cervantes,1605,1023",
    "Bülbülü Öldürmek,Harper Lee,1960,336",
    "Anna Karenina,Leo Tolstoy,1877,964",
    "Gurur ve Önyargı,Jane Austen,1813,432",
    "Karamazov Kardeşler,Fyodor Dostoyevski,1880,824",
    "Kırmızı Pazartesi,Gabriel Garcia Marquez,1981,272",
    "Küçük Prens,Antoine de Saint-Exupéry,1943,93",
    "Sherlock Holmes Sir Arthur Conan Doyle,1887,346",
    "Dracula,Bram Stoker,1897,418",
    "Dönüşüm,Franz Kafka,1915,55",
    "Büyücü,John Fowles,1965,608",
    "Gölge Oyunları,Orhan Pamuk,1990,426",
    "Melezlerin Uyanışı,Leigh Bardugo,2012,350"
]

with open("books.txt", "w") as file:
    for book_info in books_info:
        file.write(book_info + "\n")
     
class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)  # Move cursor to the beginning of the file
        books = self.file.readlines()
        if not books:
            print("No books available.")
        else:
            print("List of Books:")
            for book in books:
                book_info = book.strip().split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        release_year = input("Enter release year: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter title of book to remove: ")
        books = self.file.readlines()
        self.file.seek(0)  # Move cursor to the beginning of the file
        books = [book for book in books if title_to_remove not in book]
        self.file.truncate(0)  # Clear the file content
        self.file.seek(0)  # Move cursor to the beginning of the file
        self.file.writelines(books)
        print("Book removed successfully.")


# Create object
lib = Library()

# Menu
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")


