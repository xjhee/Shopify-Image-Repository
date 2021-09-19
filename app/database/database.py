import sqlite3
import os

class DatabaseMethods():
    """ Initialize cursors and database connection """
    def __init__(self):
        self.sqliteConnection = sqlite3.connect('databases.db')
        self.cursor = self.sqliteConnection.cursor()


            
    """ Create tables """
    def create_tables(self):
        try:
            sqlite_create_table_query = '''CREATE TABLE products (
                                        id INTEGER PRIMARY KEY,
                                        name TEXT NOT NULL,
                                        photo BLOB NOT NULL,
                                        price INT NOT NULL, 
                                        stock INT NOT NULL);'''

            print("Successfully Connected to SQLite")
            self.cursor.execute(sqlite_create_table_query)
            self.sqliteConnection.commit()
            print("SQLite table created")

            self.cursor.close()
        except sqlite3.Error as error:
            print("Error while creating a sqlite table", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("sqlite connection is closed")


    """ Convert binary format to images or files data """
    def convert_data(self, data, file_name):
        dir_path = os.path.dirname(os.path.realpath(__file__)) + file_name
        if not os.path.exists(dir_path ):
            open(dir_path, 'w').close()
        with open(dir_path, 'wb') as file:
            file.write(data)
        return file_name


    """ Display products table """
    def show_tables(self):
        self.cursor.execute("SELECT * FROM products")
        rows = self.cursor.fetchall()

        products = []
        for row in rows:
            image = self.convert_data(row[2],  '/../static/images/' + row[1] + '.png')
            products.append({
                "id":    row[0],
                "name":  row[1],
                "photo": "/%s" % (image),
                "price": row[3],
                "stock": row[4],
            })
        return products


    """ Display transactions table """
    def display_sales(self):
        self.cursor.execute("SELECT SUM(value) FROM transactions")
        result = self.cursor.fetchone()[0]
        earnings = result if result else 0
        return earnings 


    """ Insert rows into tables"""
    def insert_blob(self, id, name, photo_file, price, stock):
        try:
            print("Connected to SQLite")
            sqlite_insert_blob_query = """ INSERT INTO products
                                    (id, name, photo, price, stock) VALUES (?, ?, ?, ?, ?)"""

            # Convert data into tuple format
            data_tuple = (id, name, photo_file, price, stock)
            self.cursor.execute(sqlite_insert_blob_query, data_tuple)
            self.sqliteConnection.commit()
            print("Image and file inserted successfully as a BLOB into a table")
            self.cursor.close()

        except sqlite3.Error as error:
            print("Failed to insert blob data into sqlite table", error)
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()
                print("the sqlite connection is closed")


    """ Search products based on product name """
    def search_products(self, name):
        self.cursor.execute("SELECT * FROM products WHERE name = ?", (name,))
        rows = self.cursor.fetchall()

        products = []
        for row in rows:
            products.append({
                "id":    row[0],
                "name":  row[1],
                "photo": "/%s" % ('/../static/images/' + row[1] + '.png'),
                "price": row[3],
                "stock": row[4],
            })
        return products


    """ Purchase products """
    def purchase_products(self, product_id):
        self.cursor.execute("SELECT id, price, stock FROM products WHERE id = ?", (product_id,))
        result = self.cursor.fetchone()

        if not result: return "Unknown product id"
        (id, price, stock) = result

        if stock <= 0: return "Product out of stock"
        else:
            self.cursor.execute("INSERT INTO transactions (timestamp, productid, value) VALUES " + \
                "(datetime(), ?, ?)", (id, price))
            self.cursor.execute("UPDATE products SET stock = stock - 1 WHERE id = ?", (product_id,))
            self.sqliteConnection.commit()
        return "Purchased successfully"



        






if __name__ == '__main__':
    pass
    """
    sqliteConnection = sqlite3.connect('databases.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")
    cursor.execute("CREATE TABLE transactions (timestamp TEXT, productid INTEGER, value INTEGER)")
    sqliteConnection.commit()
    """