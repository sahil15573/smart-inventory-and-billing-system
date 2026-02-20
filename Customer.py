import psycopg2 
from database import conn

class Customer:
    def __init__(self, name=None, contact=None):
        self.name = name
        self.contact = contact
    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                contact VARCHAR(20) NOT NULL
            )"""
        )
        conn.commit()
        cur.close()
    @staticmethod
    def insert_customer(name,contact):
        cur = conn.cursor()
        cur.execute(
            """Insert INTO customers (name,contact) 
            VALUES (%s,%s)""",
            (name,contact),
        )
        conn.commit()
        cur.close()
    @staticmethod
    def update_customer(customer_id, name=None, contact=None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
        customer = cur.fetchone()
        if not customer:
            print("Customer not found")
            cur.close()
            return
        update_fields = []
        if name:
            update_fields.append(f"name = '{name}'")
        if contact:
            update_fields.append(f"contact = '{contact}'")
        update_query = f"UPDATE customers SET {','.join(update_fields)} WHERE id = {customer_id}"
        
        cur.execute(update_query, (customer_id,))
        conn.commit()
        cur.close()
    @staticmethod
    def delete_customer(customer_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM customers WHERE id = %s", (customer_id,))
        conn.commit()
        cur.close()
    @staticmethod
    def get_all_customers():
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        customers = cur.fetchall()
        cur.close()
        return customers
    @staticmethod
    def customer_menu():
        customer = Customer()
        while True:
            print("0. Exit")
            print("1. Create Table")
            print("2. Insert Customer")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. View Customer")
            choice = input("Enter your choice: ")
            if choice == "1":
                customer.create_table()
                print("Customer table created successfully")
            elif choice == "2":
                name = input("Enter customer name: ")
                contact = input("Enter customer contact: ")
                customer.insert_customer(name, contact)
                print("Customer inserted successfully")
            elif choice == "3":
                customer_id = int(input("Enter customer ID to update: "))
                name = input("Enter new name (blank if you do not want to change): ")
                contact = input("Enter new contact (blank if you do not want to change): ")
                customer.update_customer(customer_id, name, contact)
                print("Customer updated successfully")
            elif choice == "4":                
                customer_id = int(input("Enter customer ID to delete: "))
                customer.delete_customer(customer_id)
                print("Customer deleted successfully")
            elif choice == "5":                
                customers = customer.get_all_customers()
                print(customers)
                print("customer fetched successfully")
            elif choice == "0":
                print("Exiting..")
                break
            else:
                print("Invalid choice. Please try again.")

#Customer().customer_menu()