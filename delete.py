
'''
import pandas as pd
import streamlit as st
from database1 import (
    view_all_customers, view_only_customer_ids, delete_customer_data,
    view_all_employees, view_only_employee_ids, delete_employee_data,
    view_all_products, view_only_product_ids, delete_product_data
)

def delete_customers():
    result = view_all_customers()
    df = pd.DataFrame(result, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])

    with st.expander("Current Customer data"):
        st.dataframe(df)

    list_of_customer_ids = [i[0] for i in view_only_customer_ids()]
    selected_customer_id = st.selectbox("Customer ID to Delete", list_of_customer_ids)

    st.warning("Do you want to delete customer with ID: {}".format(selected_customer_id))

    if st.button("Delete Customer"):
        delete_customer_data(selected_customer_id)
        st.success("Customer has been deleted successfully")

    new_result = view_all_customers()
    df2 = pd.DataFrame(new_result, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])

    with st.expander("Updated Customer data"):
        st.dataframe(df2)

def delete_employees():
    result = view_all_employees()
    df = pd.DataFrame(result, columns=['Employee ID', 'Name', 'Salary', 'Contact Info','Employee Type','Department'])

    with st.expander("Current Employee data"):
        st.dataframe(df)

    list_of_employee_ids = [i[0] for i in view_only_employee_ids()]
    selected_employee_id = st.selectbox("Employee ID to Delete", list_of_employee_ids)

    st.warning("Do you want to delete employee with ID: {}".format(selected_employee_id))

    if st.button("Delete Employee"):
        delete_employee_data(selected_employee_id)
        st.success("Employee has been deleted successfully")

    new_result = view_all_employees()
    df2 = pd.DataFrame(new_result, columns=['Employee ID', 'Name', 'Salary', 'Contact Info','Employee Type','Department'])

    with st.expander("Updated Employee data"):
        st.dataframe(df2)

def delete_products():
    result = view_all_products()
    df = pd.DataFrame(result, columns=['Product ID', 'Type', 'Quantity', 'Price', 'Name'])

    with st.expander("Current Product data"):
        st.dataframe(df)

    list_of_product_ids = [i[0] for i in view_only_product_ids()]
    selected_product_id = st.selectbox("Product ID to Delete", list_of_product_ids)

    st.warning("Do you want to delete product with ID: {}".format(selected_product_id))

    if st.button("Delete Product"):
        delete_product_data(selected_product_id)
        st.success("Product has been deleted successfully")

    new_result = view_all_products()
    df2 = pd.DataFrame(new_result, columns=['Product ID', 'Type', 'Quantity', 'Price', 'Name'])

    with st.expander("Updated Product data"):
        st.dataframe(df2)

if __name__ == '__main__':
    entity = st.sidebar.radio("Choose entity to delete", ["Customers", "Employees", "Products"])

    if entity == "Customers":
        delete_customers()
    elif entity == "Employees":
        delete_employees()
    elif entity == "Products":
        delete_products() '''

import pandas as pd
import streamlit as st
from database1 import (
    view_all_customers, view_only_customer_ids, delete_customer_data,
    view_all_employees, view_only_employee_ids, delete_employee_data,
    view_all_products, view_only_product_ids, delete_product_data
)

def delete_customers():
    result = view_all_customers()
    df = pd.DataFrame(result, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])

    with st.expander("Current Customer data"):
        st.dataframe(df)

    list_of_customer_ids = [i[0] for i in view_only_customer_ids()]
    selected_customer_id = st.selectbox("Customer ID to Delete", list_of_customer_ids)

    st.warning("Do you want to delete customer with ID: {}".format(selected_customer_id))

    if st.button("Delete Customer"):
        delete_customer_data(selected_customer_id)
        st.success("Customer has been deleted successfully")

    new_result = view_all_customers()
    df2 = pd.DataFrame(new_result, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])

    with st.expander("Updated Customer data"):
        st.dataframe(df2)

def delete_employees():
    result = view_all_employees()
    df = pd.DataFrame(result, columns=['Employee ID', 'Name', 'Salary', 'Contact Info','Employee_type','Department'])

    with st.expander("Current Employee data"):
        st.dataframe(df)

    list_of_employee_ids = [i[0] for i in view_only_employee_ids()]
    selected_employee_id = st.selectbox("Employee ID to Delete", list_of_employee_ids)

    st.warning("Do you want to delete employee with ID: {}".format(selected_employee_id))

    if st.button("Delete Employee"):
        delete_employee_data(selected_employee_id)
        st.success("Employee has been deleted successfully")

    new_result = view_all_employees()
    df2 = pd.DataFrame(new_result, columns=['Employee ID', 'Name', 'Salary', 'Contact Info','Employee_type','Department'])

    with st.expander("Updated Employee data"):
        st.dataframe(df2)

def delete_products():
    result = view_all_products()
    df = pd.DataFrame(result, columns=['Product ID', 'Quantity',  'Name','Type','Price','Total_Val'])

    with st.expander("Current Product data"):
        st.dataframe(df)

    list_of_product_ids = [i[0] for i in view_only_product_ids()]
    selected_product_id = st.selectbox("Product ID to Delete", list_of_product_ids)

    st.warning("Do you want to delete product with ID: {}".format(selected_product_id))

    if st.button("Delete Product"):
        delete_product_data(selected_product_id)
        st.success("Product has been deleted successfully")

    new_result = view_all_products()
    df2 = pd.DataFrame(new_result, columns=['Product ID', 'Quantity', 'Name', 'Type', 'Price','Total_Val'])

    with st.expander("Updated Product data"):
        st.dataframe(df2)

if __name__ == '__main__':
    entity = st.sidebar.radio("Choose entity to delete", ["Customers", "Employees", "Products"])

    if entity == "Customers":
        delete_customers()
    elif entity == "Employees":
        delete_employees()
    elif entity == "Products":
        delete_products()




