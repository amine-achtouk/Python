library = [
    {  "title": "Python Basics",  "author": "John Smith",  "price": 120,  "quantity": 3,  "genre": "Programming",  "year": 2021 },
    {  "title": "Learn Java",  "author": "Sarah Lee",  "price": 90,  "quantity": 5,  "genre": "Programming",  "year": 2020 },
    {  "title": "World History",  "author": "Mark Brown",  "price": 70,  "quantity": 2,  "genre": "History",  "year": 2018 }
]


def show_books(library):
    for book in library:
        print(f"Title : {book['title']} || Author : {book['author']} || Price : {book['price']} || quantity : {book['quantity']} || genre : {book['genre']} || year : {book['year']}")


def available_books(library):
    for book in library:
        if book["quantity"] > 0:
            print(f"Title : {book['title']} || Price : {book['price']}")


def search_book(library):
    search = input('Search Book Title : ')
    for book in library:
        if search == book["title"]:
            print(f"Title : {book['title']} || Author : {book['author']} || Price : {book['price']} || quantity : {book['quantity']} || genre : {book['genre']} || year : {book['year']}")
            return
    print("❌ Book Not Found")



def borrow_book(library):
    search = input('Search Book : ')
    for book in library:
        if search == book["title"]:
            if book["quantity"] > 0:
                book["quantity"]  -= 1
                print(f"Title : {book['title']} || Author : {book['author']} || Price : {book['price']} || quantity : {book['quantity']} || genre : {book['genre']} || year : {book['year']}")
            elif book["quantity"] == 0:
                print('❌ Book out of stock')    
            return  
    print("❌ Book Not Found")      


def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    genre = input("Enter genre: ")
    year = int(input("Enter year: "))
    
    new_book = {
        "title": title,
        "author": author,
        "price": price,
        "quantity": quantity,
        "genre": genre,
        "year": year
    }
    library.append(new_book)
    print("✅ Book added successfully!")
    print(f"Title : {new_book['title']} || Author : {new_book['author']} || Price : {new_book['price']} || quantity : {new_book['quantity']} || genre : {new_book['genre']} || year : {new_book['year']}")

    




while True:
    print("\n📚 LIBRARY MENU")
    print("1. Show all books")
    print("2. Show available books")
    print("3. Search for a book")
    print("4. Borrow a book")
    print("5. Add a book")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_books(library)
    elif choice == "2":
        available_books(library)
    elif choice == "3": 
        search_book(library)
    elif choice == "4":
        borrow_book(library)
    elif choice == "5":
        add_book(library)
    elif choice == "0":
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice, try again.")





