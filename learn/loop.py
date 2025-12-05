# person = {
#     "name": "Ali",
#     "age": 25,
#     "grade": "18"
# }

# person['city'] = 'agadir'

# person["grade"] = 19

# del person["age"]

# for key, value in person.items():
#     print(f'{key} : {value}')

library = [
    {"title": "Python Basics", "author": "John Smith", "price": 120, "quantity": 3},
    {"title": "Learn Java", "author": "Sarah Lee", "price": 90, "quantity": 0},
    {"title": "Web Development", "author": "Mark Davis", "price": 150, "quantity": 5},
]

total_value = 0

def show_books(library):
    for book in library:
        title = book["title"]
        author = book["author"]
        price = book["price"]
        quantity = book["quantity"]
        print(f"📘 Book: {title} | Author: {author} | Price: {price} | Quantity: {quantity}")




def available_books(library):
    for book in library:
        title = book["title"]
        quantity = book["quantity"]
        if quantity > 0:
            print(f'this book ({title}) is available')

total_value = 0

def calcu_total(library):
    for book in library:
        title = book["title"]
        price = book["price"]
        quantity = book["quantity"]
        total_value = quantity * price
        if quantity > 0:
            print(f'total value for this book {title} is {total_value}$')



def add_book(library, title, author, price, quantity):
    new_book = {
        "title": title,
        "author": author,
        "price": price,
        "quantity": quantity
    }
    library.append(new_book)
    print(f"✅ Book '{title}' added successfully!")







available_books(library)
print('--------------------------')
show_books(library)
print('--------------------------')
calcu_total(library)
print('--------------------------')
add_book(library, "C Programming", "Dennis Ritchie", 100, 7)
