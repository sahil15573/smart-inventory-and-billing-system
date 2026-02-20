#Sales -> Columns: id, customer_id, date, total_amount
import psycopg2
from database import conn
class Sale:
    @staticmethod
    def __init__(customer_id, date, total_amount):
        customer_id = customer_id
        date = date
        total_amount = total_amount
    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS sales (
                        id SERIAL PRIMARY KEY,
                        customer_id INTEGER NOT NULL,
                        date DATE NOT NULL,
                        total_amount DECIMAL(10, 2) NOT NULL,
                        CONSTRAINT fk_sales_customer
                            FOREIGN KEY(customer_id)
                            REFERENCES customers(id)
                            ON DELETE CASCADE
                    )''')
        conn.commit()
        cur.close()
    @staticmethod
    def insert_sale(customer_id, date, total_amount):
        cur = conn.cursor()
        cur.execute('''INSERT INTO sales (customer_id, date, total_amount)
                       VALUES (%s, %s, %s)''',
                    (customer_id, date, total_amount))
        conn.commit()
        cur.close()
    @staticmethod
    def update_inventory(product_id, quantity_sold):
     cur = conn.cursor()
     cur.execute("SELECT quantity FROM products WHERE id = %s", (product_id,))
     result = cur.fetchone()

     if not result:
         print("Product not found")
         cur.close()
         return
 
     available_quantity = result[0]

     if quantity_sold > available_quantity:
         print("Not enough stock available")
         cur.close()
         return

     cur.execute("""
         UPDATE products
         SET quantity = quantity - %s
         WHERE id = %s
     """, (quantity_sold, product_id))

     conn.commit()
     cur.close()

     print("Inventory updated successfully")
    @staticmethod
    def delete_sale(sale_id):
     cur = conn.cursor()

    # Step 1: Check if sale exists
     cur.execute("SELECT id FROM sales WHERE id = %s", (sale_id,))
     sale = cur.fetchone()

     if not sale:
         print("Sale not found")
         cur.close()
         return

    # Step 2: Get sale items to restore inventory
     cur.execute("""
         SELECT product_id, quantity
         FROM sale_items
         WHERE sale_id = %s
     """, (sale_id,))
     items = cur.fetchall()

    # Step 3: Restore inventory
     for product_id, quantity in items:
         cur.execute("""
             UPDATE products
             SET quantity = quantity + %s
             WHERE id = %s
         """, (quantity, product_id))

    # Step 4: Delete sale items
     cur.execute("DELETE FROM sale_items WHERE sale_id = %s", (sale_id,))

    # Step 5: Delete sale
     cur.execute("DELETE FROM sales WHERE id = %s", (sale_id,))

     conn.commit()
     cur.close()

     print("Sale deleted and inventory restored successfully")
    @staticmethod
    def view_sales():
        cur = conn.cursor()
        cur.execute('SELECT * FROM sales')
        sales = cur.fetchall()
        for sale in sales:
            print(sale)
        cur.close()
    @staticmethod
    def view_sale_by_id(sale_id):
        cur = conn.cursor()
        cur.execute('SELECT * FROM sales WHERE id = %s', (sale_id,))
        sale = cur.fetchone()
        print(sale)
        cur.close()
    @staticmethod
    def generate_bill(sale_id):
        cur = conn.cursor()
        cur.execute('SELECT * FROM sale_items WHERE sale_id = %s', (sale_id,))
        SaleItem = cur.fetchall()
        print("Bill for Sale ID:", sale_id)
        total_amount = 0
        for item in SaleItem:
            print("Product ID:", item[2], "Quantity:", item[3], "Price:", item[4])
            total_amount += item[4] * item[3]
        print("Total Amount:", total_amount)
        cur.close()
        return total_amount
    
#----------Analytical Queries----------#
    @staticmethod
    def get_total_sales_by_date(start_date, end_date):
        cur = conn.cursor()
        cur.execute('''SELECT SUM(total_amount) FROM sales
                       WHERE date BETWEEN %s AND %s''',
                    (start_date, end_date))
        total_sales = cur.fetchone()[0]
        cur.close()
        return total_sales
    @staticmethod
    def get_top_selling_products():
        cur = conn.cursor()
        cur.execute('''SELECT product_id, SUM(quantity) as total_quantity
                       FROM sale_items
                       GROUP BY product_id
                       ORDER BY total_quantity DESC
                       LIMIT 5''')
        top_products = cur.fetchall()
        cur.close()
        return top_products
    @staticmethod
    def get_sales_by_customer(customer_id):
        cur = conn.cursor()
        cur.execute('SELECT * FROM sales WHERE customer_id = %s', (customer_id,))
        sales = cur.fetchall()
        for sale in sales:
            print(sale)
        cur.close()
        return sales
    @staticmethod
    def sale_menu():
        while True:
            print("1. Create Table")
            print("2. Insert Sale")
            print("3. Update Inventory")
            print("4. Delete Sale")
            print("5. View Sales")
            print("6. View Sale by ID")
            print("7. Generate Bill")
            print("8. Get Total Sales by Date")
            print("9. Get Top Selling Products")
            print("10. Get Sales by Customer")
            print("0. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                Sale.create_table()
                print("Table created")
            elif choice == '2':
                customer_id = int(input("Enter customer id: "))
                date = input("Enter date: ")
                total_amount = float(input("Enter total amount: "))
                Sale.insert_sale(customer_id, date, total_amount)
                print("Sale inserted")

            elif choice == '3':
                product_id = int(input("Enter product id: "))
                quantity_sold = int(input("Enter quantity sold: "))
                Sale.update_inventory(product_id, quantity_sold)

            
            elif choice == '4':
                sale_id = int(input("Enter sale id: "))
                Sale.delete_sale(sale_id)
                print("Sale deleted")
            
            elif choice == '5':
                Sale.view_sales()
                print("Sales viewed")
            
            elif choice == '6':
                sale_id = int(input("Enter sale id: "))
                Sale.view_sale_by_id(sale_id)
                print("Sale viewed by ID")

            elif choice == '7':
                sale_id = int(input("Enter sale id: "))
                total_amount = Sale.generate_bill(sale_id)
                print("Total Amount:", total_amount)
            elif choice == '8':
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                total_sales = Sale.get_total_sales_by_date(start_date, end_date)
                print("Total Sales from", start_date, "to", end_date, "is:", total_sales)
            elif choice == '9':
                top_products = Sale.get_top_selling_products()
                print("Top Selling Products:")
                for product in top_products:
                    print("Product ID:", product[0], "Total Quantity Sold:", product[1])
            elif choice == '10':
                customer_id = int(input("Enter customer id: "))
                sales = Sale.get_sales_by_customer(customer_id)
                print("Sales for Customer ID:", customer_id)
                for sale in sales:
                    print(sale)
                    print("Total Amount:", Sale.generate_bill(sale[0]))
            
            elif choice == '0':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.") 
#Sale.sale_menu()