
import pandas as pd
import streamlit as st
from database1 import (
    view_all_customers, delete_customer_data, update_customer_data, view_only_customer_ids, 
    view_all_employees, view_only_employee_ids, delete_employee_data,update_employee_data,
    view_all_products, view_only_product_ids, delete_product_data, update_product_data
)

def update_customer():
    result = view_all_customers()
    df = pd.DataFrame(result, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])

    with st.expander("Current Customer data"):
        st.dataframe(df)

    list_of_customers_id = [i[0] for i in view_only_customer_ids()]
    selected_customer_id = st.selectbox("Customer ID to Update", list_of_customers_id)

    st.warning("Choose new details for customer with ID: {}".format(selected_customer_id))

    new_first_name = st.text_input("New First Name:")
    new_last_name = st.text_input("New Last Name:")
    new_email = st.text_input("New Email:")
    new_phone_no = st.text_input("New Phone Number:")

    if st.button("Update Customer"):
        updated_data = update_customer_data(selected_customer_id, new_first_name, new_last_name, new_email, new_phone_no)

        if updated_data:
            st.success("Customer data has been updated successfully.")
            df_updated = pd.DataFrame(updated_data, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])

            with st.expander("Updated Customer data"):
                st.dataframe(df_updated)


def update_employee():
    result = view_all_employees()
    df = pd.DataFrame(result, columns=['Employee ID', 'Name', 'Salary', 'Contact Info','Employee Type','Department'])

    with st.expander("Current Employee data"):
        st.dataframe(df)

    list_of_employees = [i[0] for i in view_only_employee_ids()]
    selected_employee_id = st.selectbox("Employee ID to Update", list_of_employees)

    st.warning("Choose new details for employee with ID: {}".format(selected_employee_id))

    new_name = st.text_input("New Name:")
    new_salary = st.text_input("New Salary:")
    new_contact_info = st.text_input("New Contact Info:")
    new_employee_type = st.text_input("New Employee Type:")
    new_department = st.text_input("New Department:")

    if st.button("Update Employee"):
        updated_data = update_employee_data(selected_employee_id, new_name, new_salary, new_contact_info,new_employee_type,new_department)

        if updated_data:
            st.success("Employee data has been updated successfully.")
            df_updated = pd.DataFrame(updated_data, columns=['Employee ID', 'Name', 'Salary', 'Contact Info','Employee Type','Department'])

            with st.expander("Updated Employee data"):
                st.dataframe(df_updated)

def update_product():
    result = view_all_products()
    df = pd.DataFrame(result,columns = ['Product ID', 'Quantity','Name',' Type', 'Price','Total_Val'])

    with st.expander("Current Product data"):
        st.dataframe(df)
    
    list_of_products = [i[0] for i in view_only_product_ids()]
    selected_product_id = st.selectbox("Product ID to update",list_of_products)

    st.warning("Choose new details for product with ID: {}".format(selected_product_id))

    new_q = st.text_input("New Quantity:")
    new_name = st.text_input("New Name:")
    new_type = st.text_input("New Type:")
    new_price = st.text_input("New Price:")

    if st.button("Update Product"):
        updated_data = update_product_data(selected_product_id, new_q, new_name, new_type, new_price)

        if updated_data:
            st.success("Product data has been updated successfully.")
            df_updated = pd.DataFrame(updated_data, columns=['Product ID', 'Quantity','Name',' Type', 'Price','Total_Val'])

            with st.expander("Updated Product data"):
                st.dataframe(df_updated)

if __name__ == '__main__':
    y = st.sidebar.radio("Choose entity to update", ["Customers", "Employees", "Products"])
    if y=="Customers":
        update_customer()
    elif y=="Employees":
        update_employee()
    elif y=="Products":
        update_product() 
'''
import pandas as pd
import streamlit as st
from database1 import (
    view_all_customers, delete_customer_data, update_customer_data, view_only_customer_ids, 
    view_all_employees, view_only_employee_ids, delete_employee_data,update_employee_data,
    view_all_products, view_only_product_ids, delete_product_data, update_product_data
)

def update_customer():
    result = view_all_customers()
    df = pd.DataFrame(result, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])

    with st.expander("Current Customer data"):
        st.dataframe(df)

    list_of_customers_id = [i[0] for i in view_only_customer_ids()]
    selected_customer_id = st.selectbox("Customer ID to Update", list_of_customers_id)

    st.warning("Choose new details for customer with ID: {}".format(selected_customer_id))

    new_first_name = st.text_input("New First Name:")
    new_last_name = st.text_input("New Last Name:")
    new_email = st.text_input("New Email:")
    new_phone_no = st.text_input("New Phone Number:")

    if st.button("Update Customer"):
        updated_data = update_customer_data(selected_customer_id, new_first_name, new_last_name, new_email, new_phone_no)

        if updated_data:
            st.success("Customer data has been updated successfully.")
            df_updated = pd.DataFrame(updated_data, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])

            with st.expander("Updated Customer data"):
                st.dataframe(df_updated)


def update_employee():
    result = view_all_employees()
    df = pd.DataFrame(result, columns=['Employee ID', 'Name', 'Salary', 'Contact Info'])

    with st.expander("Current Employee data"):
        st.dataframe(df)

    list_of_employees = [i[0] for i in view_only_employee_ids()]
    selected_employee_id = st.selectbox("Employee ID to Update", list_of_employees)

    st.warning("Choose new details for employee with ID: {}".format(selected_employee_id))

    new_name = st.text_input("New Name:")
    new_salary = st.text_input("New Salary:")
    new_contact_info = st.text_input("New Contact Info:")

    if st.button("Update Employee"):
        updated_data = update_employee_data(selected_employee_id, new_name, new_salary, new_contact_info)

        if updated_data:
            st.success("Employee data has been updated successfully.")
            df_updated = pd.DataFrame(updated_data, columns=['Employee ID', 'Name', 'Salary', 'Contact Info'])

            with st.expander("Updated Employee data"):
                st.dataframe(df_updated)

def update_product():
    result = view_all_products()
    df = pd.DataFrame(result,columns = ['Product ID', 'Quantity','Name',' Type', 'Price'])

    with st.expander("Current Product data"):
        st.dataframe(df)
    
    list_of_products = [i[0] for i in view_only_product_ids()]
    selected_product_id = st.selectbox("Product ID to update",list_of_products)

    st.warning("Choose new details for product with ID: {}".format(selected_product_id))

    new_q = st.text_input("New Quantity:")
    new_name = st.text_input("New Name:")
    new_type = st.text_input("New Type:")
    new_price = st.text_input("New Price:")

    if st.button("Update Product"):
        updated_data = update_product_data(selected_product_id, new_q, new_name, new_type, new_price)

        if updated_data:
            st.success("Product data has been updated successfully.")
            df_updated = pd.DataFrame(updated_data, columns=['Product ID', 'Quantity','Name',' Type', 'Price'])

            with st.expander("Updated Product data"):
                st.dataframe(df_updated)

if __name__ == '__main__':
    y = st.sidebar.radio("Choose entity to update", ["Customers", "Employees", "Products"])
    if y=="Customers":
        update_customer()
    elif y=="Employees":
        update_employee()
    elif y=="Products":
        update_product()
'''


