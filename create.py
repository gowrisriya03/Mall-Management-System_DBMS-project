

'''import streamlit as st
from database1 import add_customer_data, add_employee_data, add_product_data

x = st.sidebar.radio("Choose", ["Customers", "Employees", "Products"])

def create_customer():
    col1, col2 = st.columns(2)
    
    with col1:
        customer_id = st.text_input("Customer ID:")
        first_name = st.text_input("First Name:")
        phone_no = st.text_input("Phone Number:")    
    with col2:
        email = st.text_input("Email:")
        last_name = st.text_input("Last Name:")
    
    if st.button("Add Customer"):
        add_customer_data(customer_id, first_name, last_name, email, phone_no)
        st.success("Successfully added Customer: {} {}".format(first_name, last_name))

def create_employee():
    col1, col2 = st.columns(2)
    
    with col1:
        employee_id = st.text_input("Employee ID:")
        name = st.text_input("Name:")
        contact_info = st.text_input("Contact Info:")
    with col2:
        salary = st.text_input("Salary:")
        employee_type = st.text_input("Employee Type:")
        department = st.text_input("Department:")

    
    if st.button("Add Employee"):
        add_employee_data(employee_id, name, salary, contact_info,employee_type,department)
        st.success("Successfully added Employee: {}".format(name))

def create_product():
    col1, col2 = st.columns(2)

    with col1:
        product_id = st.text_input("Product ID:")
        name = st.text_input("Name:")
        type = st.text_input("Type:")
    with col2:
        price = st.text_input("Price:")
        quantity = st.text_input("Quantity:")

    if st.button("Add Product"):
        add_product_data(product_id, quantity, name, type, price)
        st.success("Successfully added Product: {}".format(name))


# Use the selected option to determine the action
if x == "Customers":
    create_customer()

elif x == "Employees":
    create_employee()

elif x=="Products":
    create_product() '''

import streamlit as st
from database1 import add_customer_data, add_employee_data, add_product_data

x = st.sidebar.radio("Choose", ["Customers", "Employees", "Products"])

def create_customer():
    col1, col2 = st.columns(2)
    
    with col1:
        customer_id = st.text_input("Customer ID:")
        first_name = st.text_input("First Name:")
        phone_no = st.text_input("Phone Number:")    
    with col2:
        email = st.text_input("Email:")
        last_name = st.text_input("Last Name:")
    
    if st.button("Add Customer"):
        add_customer_data(customer_id, first_name, last_name, email, phone_no)
        st.success("Successfully added Customer: {} {}".format(first_name, last_name))

def create_employee():
    col1, col2 = st.columns(2)
    
    with col1:
        employee_id = st.text_input("Employee ID:")
        name = st.text_input("Name:")
        contact_info = st.text_input("Contact Info:")
        employee_type = st.text_input("Employee Type:")
        Department = st.text_input("Department:")  # Add department input field
    with col2:
        salary = st.text_input("Salary:")
    
    if st.button("Add Employee"):
        add_employee_data(employee_id, name, salary, contact_info, employee_type, Department)
        st.success("Successfully added Employee: {}".format(name))

def create_product():
    col1, col2 = st.columns(2)

    with col1:
        product_id = st.text_input("Product ID:")
        name = st.text_input("Name:")
        type = st.text_input("Type:")
    with col2:
        price = st.text_input("Price:")
        quantity = st.text_input("Quantity:")

    if st.button("Add Product"):
        add_product_data(product_id, quantity, name, type, price)
        st.success("Successfully added Product: {}".format(name))


# Use the selected option to determine the action
if x == "Customers":
    create_customer()

elif x == "Employees":
    create_employee()

elif x == "Products":
    create_product()


