import sqlite3
from flask import Flask , request, jsonify
class Smartphone:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()

    def sql_get_all_smartphones(self):

        self.cursor.execute("SELECT * FROM smartphone")
        data = self.cursor.fetchall()
        res = {}
        for id , name , color , ram , memory, price in data:
            res[id]={
                'name': name,
                'color' : color,
                'RAM' : ram,
                'memory':memory,
                'price': price}
        return res
    
    def sql_get_product_by_id(self, id):
        self.cursor.execute("SELECT * FROM smartphone WHERE id=?",(id,))
        return self.cursor.fetchall()
        
    
    def sql_get_smartphone_by_name(self, name):
        self.cursor.execute("SELECT * FROM smartphone WHERE name=?",(name,))
        return self.cursor.fetchall()
    
    def sql_get_smartphone_all_names(self):
        self.cursor.execute("SELECT name FROM smartphone")
        data = self.cursor.fetchall()
        return [res[0] for res in data]
    
    def sql_get_smartphone_by_color(self, color):
        self.cursor.execute("SELECT * FROM smartphone WHERE color = ?",(color,))
        data = self.cursor.fetchall()
        return list(map(list,data))
    
    def sql_get_smartphone_by_ram(self, ram):
        self.cursor.execute("SELECT * FROM smartphone WHERE ram = ?",(ram,))
        data = self.cursor.fetchall()
        return list(map(list,data))
    
    def sql_get_smartphone_by_memory(self, memory):
        self.cursor.execute("SELECT * FROM smartphone WHERE memory = ?",(memory,))
        data = self.cursor.fetchall()
        return list(map(list,data))
    
    def sql_get_smartphone_by_price(self, price):
        self.cursor.execute("SELECT * FROM smartphone WHERE price < ?",(price,))
        data = self.cursor.fetchall()
        return list(map(list,data))
    
    def sql_add_smartphone(self, phone):
        name, color, ram, memory, price = phone 
        self.cursor.execute(
            "INSERT INTO smartphone (name, color, ram, memory, price) VALUES (?, ?, ?, ?, ?)",
            ( name, color, ram, memory, price),
        )
        self.connect.commit()
        return True
    
    def sql_delete_smartphone(self, id):

        return 
db1 = Smartphone('smartphone_store.db')
print(db1.sql_get_smartphone_by_ram('6GB'))