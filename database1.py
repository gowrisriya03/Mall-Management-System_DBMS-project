

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sriya@2003",
    database="mall_management"
)

c = mydb.cursor()
def totalproduct():
    c.execute('select mall_management.updateTotalValue();')
    dumm_int = c.fetchall()
    mydb.commit()
    c.execute('SELECT * from product')
    data = c.fetchall()
    return data

def create_customer_table():
    c.execute('CREATE TABLE IF NOT EXISTS CUSTOMER('
              'customer_id INT AUTO_INCREMENT PRIMARY KEY, '
              'first_name VARCHAR(255), '
              'last_name VARCHAR(255), '
              'email VARCHAR(255), '
              'phone_no VARCHAR(15))')

def add_customer_data(customer_id, first_name, last_name, email, phone_no):
    c.execute('INSERT INTO CUSTOMER(customer_id, first_name, last_name, email, phone_no) VALUES (%s, %s, %s, %s, %s)',
              (customer_id, first_name, last_name, email, phone_no))
    mydb.commit()

def view_all_customers():
    c.execute('SELECT * FROM CUSTOMER')
    data = c.fetchall()
    return data

def view_only_customer_names():
    c.execute('SELECT first_name, last_name FROM CUSTOMER')
    data = c.fetchall()
    return data

def view_only_customer_ids():
    c.execute('SELECT customer_id FROM CUSTOMER')
    data = c.fetchall()
    return data

def get_customer(customer_id):
    c.execute('SELECT * FROM CUSTOMER WHERE customer_id = %s', (customer_id,))
    data = c.fetchall()
    return data

def update_customer_data(customer_id, new_first_name, new_last_name, new_email, new_phone_no):
    try:
        c.execute("UPDATE CUSTOMER SET first_name=%s, last_name=%s, email=%s, phone_no=%s WHERE customer_id=%s",
                  (new_first_name, new_last_name, new_email, new_phone_no, customer_id))
        mydb.commit()
        print("Customer data updated successfully.")

        # Return the updated data for display
        c.execute('SELECT * FROM CUSTOMER WHERE customer_id = %s', (customer_id,))
        updated_data = c.fetchall()
        return updated_data

    except Exception as e:
        print("Error updating customer data:", str(e))
        return None



def delete_customer_data(customer_id):
    try:
        c.execute('DELETE FROM CUSTOMER WHERE customer_id = %s', (customer_id,))
        mydb.commit()
        print("Customer deleted successfully.")
    except Exception as e:
        print("Error deleting customer:", str(e))

def create_employee_table():
    c.execute('CREATE TABLE IF NOT EXISTS EMPLOYEE('
              'employee_id INT AUTO_INCREMENT PRIMARY KEY, '
              'name VARCHAR(255), '
              'salary DECIMAL(10, 2), '
              'contact_info VARCHAR(255), '
              'employee_type VARCHAR(255), '
              'Department VARCHAR(255))')

def add_employee_data(employee_id, name, salary, contact_info, employee_type, Department):
    c.execute('INSERT INTO EMPLOYEE(employee_id, name, salary, contact_info, employee_type, Department) VALUES (%s, %s, %s, %s, %s, %s)',
              (employee_id, name, salary, contact_info, employee_type, Department))
    mydb.commit()

                              
def view_all_employees():
    c.execute('SELECT * FROM EMPLOYEE')
    data = c.fetchall()
    return data



def view_only_employee_names():
    c.execute('SELECT name FROM EMPLOYEE')
    data = c.fetchall()
    return data

def view_only_employee_ids():
    c.execute('SELECT employee_id FROM EMPLOYEE')
    data = c.fetchall()
    return data

def get_employee(employee_id):
    c.execute('SELECT * FROM EMPLOYEE WHERE employee_id = %s', (employee_id,))
    data = c.fetchall()
    return data

def update_employee_data(employee_id, new_name, new_salary, new_contact_info, new_employee_type, new_Department):
    try:
        c.execute("UPDATE EMPLOYEE SET name=%s, salary=%s, contact_info=%s, employee_type=%s, Department=%s "
                  "WHERE employee_id=%s",
                  (new_name, new_salary, new_contact_info, new_employee_type, new_Department, employee_id))
        mydb.commit()
        print("Employee data updated successfully.")

        # Return the updated data for display
        c.execute('SELECT * FROM EMPLOYEE WHERE employee_id = %s', (employee_id,))
        updated_data = c.fetchall()
        return updated_data
    except Exception as e:
        print("Error updating Employee data:", str(e))
        return None

def delete_employee_data(employee_id):
    try:
        c.execute('DELETE FROM EMPLOYEE WHERE employee_id = %s', (employee_id,))
        mydb.commit()
        print("Employee deleted successfully.")
    except Exception as e:
        print("Error deleting employee:", str(e))

# Create the product table
def create_product_table():
    c.execute('CREATE TABLE IF NOT EXISTS PRODUCT('
              'product_id INT AUTO_INCREMENT PRIMARY KEY, '
              'quantity INT, '
              'name VARCHAR(255), '
              'type VARCHAR(255), '
              'price DECIMAL(10, 2))')

# Add product data to the table
def add_product_data(product_id, quantity, name, type, price):
    c.execute('INSERT INTO PRODUCT(product_id, quantity, name, type, price) VALUES (%s, %s, %s, %s, %s)',
              (product_id, quantity, name, type, price))
    mydb.commit()

# View all products in the table
def view_all_products():
    c.execute('SELECT * FROM PRODUCT')
    data = c.fetchall()
    return data

# View only product names
def view_only_product_names():
    c.execute('SELECT name FROM PRODUCT')
    data = c.fetchall()
    return data

def view_only_product_ids():
    c.execute('SELECT product_id FROM PRODUCT')
    data = c.fetchall()
    return data

# Get product by product_id
def get_product(product_id):
    c.execute('SELECT * FROM PRODUCT WHERE product_id = %s', (product_id,))
    data = c.fetchall()
    return data

def update_product_data(product_id, new_q, new_name, new_type, new_price):
    try:
        c.execute("UPDATE PRODUCT SET quantity=%s, name=%s, type=%s , price = %s WHERE product_id=%s",
                  (new_q, new_name, new_type, new_price, product_id))
        mydb.commit()
        print("Product data updated successfully.")

        # Return the updated data for display
        c.execute('SELECT * FROM PRODUCT WHERE product_id = %s', (product_id,))
        updated_data = c.fetchall()
        return updated_data
    except Exception as e:
        print("Error updating Product data:", str(e))
        return None
    
# Delete product data by product_id
def delete_product_data(product_id):
    try:
        c.execute('DELETE FROM PRODUCT WHERE product_id = %s', (product_id,))
        mydb.commit()
        print("Product deleted successfully.")
    except Exception as e:
        print("Error deleting product:", str(e))

def close():
    c.close()
    mydb.close()

