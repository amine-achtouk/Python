# person = {
#     "name": "Ali",
#     "age": 25,
#     "city": "Casablanca"
#     }

# for key in person:
#     print( key, ':',person[key])

# grades = {"Math": 90, "Physics": 85, "Chemistry": 95}

# for module, score in grades.items():
#     print(module, ':', score)

# fruits = {"apple": 5, "banana": 8, "orange": 12}

# for fruit, quantity in fruits.items():
#     print('fruit : ',fruit, '  Quantity : ', quantity  )






# products = {
#     "pen": 10,
#     "notebook": 3,
#     "eraser": 0,
#     "pencil": 5,
    
# }

# for product,quantity  in products.items():
#     if quantity > 0 :
#         print(f"✅ {product} is available ({quantity} in stock)")
#     else:
#         print(f"❌ {product} is out of stock")    




products = [
    {"name": "pen", "quantity": 10, "price": 2},
    {"name": "notebook", "quantity": 0, "price": 5},
    {"name": "eraser", "quantity": 5, "price": 1},
    {"name": "pencil", "quantity": 3, "price": 1.5}
]

def Chek_store(products):
    for product in products:
        if product['quantity'] > 0:
            print(f'✅ Product {product["name"]} is available: {product["quantity"]} in stock, Price: ${product["price"]}')
        else:
            print('❌ Product notebook is out of stock"')


Chek_store(products)            
