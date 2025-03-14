
from flask import Flask, request
from db import *
app = Flask(__name__)
## view all smartphone
db1 = Smartphone('smartphone_store.db')
@app.route('/smartphones', methods=['GET'])
def get_all_smartphones():
    """Returns all smartphones in the database"""
    db1 = Smartphone('smartphone_store.db')
    data = db1.sql_get_all_smartphones()
    return data
# view all smartphones by id
@app.route('/smartphones/id/<int:id>', methods=['GET'])
def get_product_by_id(id):
    """Returns smartphones in the database by id"""
    db1 = Smartphone('smartphone_store.db')
    data = db1.sql_get_product_by_id(id)
    return data

# view smartphone by name
@app.route('/smartphones/name/<name>', methods=['GET'])
def get_smartphone_by_name(name):
    """Returns a product by name"""
    db1 = Smartphone('smartphone_store.db')

    return db1.sql_get_smartphone_by_name(name)

# view all smartphones names
@app.route('/smartphones/names', methods=['GET'])
def get_smartphone_all_names():
    """Returns all smartphones names"""
    db1 = Smartphone('smartphone_store.db')

    return db1.sql_get_smartphone_all_names()

# view smartphone by color
@app.route('/smartphones/color/<color>', methods=['GET'])
def get_smartphone_by_color(color):
    """Returns a smartphones by color"""
    db1 = Smartphone('smartphone_store.db')

    return db1.sql_get_smartphone_by_color(color)

# view smartphone by ram
@app.route('/smartphones/ram/<ram>', methods=['GET'])
def get_smartphone_by_ram(ram):
    """Returns a smartphones by ram"""
    db1 = Smartphone('smartphone_store.db')
    return db1.sql_get_smartphone_by_ram(ram)

# view smartphone by memory
@app.route('/smartphones/memory/<int:memory>', methods=['GET'])
def get_smartphone_by_memory(memory):
    """Returns a smartphones by memory"""
    return db1.sql_get_smartphone_by_memory(memory)

# view smartphone by price
@app.route('/smartphones/price/<float:price>', methods=['GET'])
def get_smartphone_by_price(price):
    """Returns a smartphones if database in price bigger from price"""
    return db1.sql_get_smartphone_by_price(price)

# view add smartphone
@app.route('/smartphone/add', methods=['POST'])
def add_smartphone():
    """Adds a product to the database"""
    db1 = Smartphone('smartphone_store.db')
    data = request.get_json()
    
    name = data.get('name')
    color = data.get('color')
    ram = data.get('ram')
    memory = data.get('memory')
    price = data.get('price')
    return {'status':db1.sql_add_smartphone((name, color, ram, memory, price))}


# view delete smartphone
@app.route('/smartphone/delete/<int:id>', methods=['DELETE'])
def delete_smartphone(id):
    """Deletes a smartphone from the database"""
    return 

if __name__ == '__main__':
    app.run(debug=True)
