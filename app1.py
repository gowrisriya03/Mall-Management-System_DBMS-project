
import streamlit as st
import mysql.connector
import pandas as pd
from create import create_customer, create_employee, create_product
from read import read_customers, read_employees, read_products
from update import update_customer, update_employee, update_product
from delete import delete_customers, delete_employees, delete_products

from database1 import totalproduct
from frontend import total_product_frontend

from database1 import (
    create_customer_table,
    add_customer_data,
    view_all_customers,
    view_only_customer_names,
    get_customer,
    update_customer_data,
    delete_customer_data,
    create_employee_table,
    add_employee_data,
    view_all_employees,
    view_only_employee_names,
    update_employee_data,
    get_employee,
    delete_employee_data,
    create_product_table,
    add_product_data,
    view_all_products,
    view_only_product_names,
    update_product_data,
    get_product,
    delete_product_data,
    close
)

# Connect to MySQL database
connection = mysql.connector.connect(
   host="localhost",
        user="root",
        password="Sriya@2003",
        database="mall_management"
)

cursor = connection.cursor()


def execute_default_query(table_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sriya@2003",
        database="mall_management"
    )
    cursor = mydb.cursor()
    
    # Default queries for each table
    default_queries = {
        "customer": "SELECT * FROM customer;",
        "employee": "SELECT * FROM employee;",
        "product": "SELECT * FROM product;"
    }
    
    query = default_queries.get(table_name, "")
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Get column names
    column_names = [i[0] for i in cursor.description]
    
    cursor.close()
    mydb.close()
    return result, column_names


# Modify your execute_nested_query function
def execute_nested_query(table_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sriya@2003",
        database="mall_management"
    )

    cursor = mydb.cursor()

    # Construct the nested query (more complex query)
    if table_name == "employee":
        query = "SELECT * FROM employee WHERE salary > (SELECT AVG(salary) FROM employee);"
    elif table_name == "product":
        query = "SELECT * FROM product WHERE price > (SELECT AVG(price) FROM product);"
    else:
        query = ""

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    mydb.close()
    return result


def execute_correlated_query(table_name):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sriya@2003",
        database="mall_management"
    )
    cursor = mydb.cursor()

     # Construct a different correlated query
    if table_name == "employee":
        query = (
            "SELECT employee_id, name, contact_info, salary "
            "FROM employee e "
            "WHERE salary > (SELECT MIN(salary) FROM employee e2 WHERE e.Department = e2.Department);"
        )
    
    else:
        query = ""

    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    mydb.close()
    return result


def display_query_result(query_result, column_names, table_name):
    st.markdown(f'<h2 style="color:blue">{table_name} Table</h2>', unsafe_allow_html=True)
    
    # Create a DataFrame from the query result and column names
    df = pd.DataFrame(query_result, columns=column_names)

    # Display the DataFrame without index column names
    st.table(df)

def display_query_result1(result, selected_columns, table_name):
    if result:
        st.write(f"Query Result for {table_name.capitalize()}:")
        # Calculate and display count
        count_result = len(result)
        st.write(f"Count: {count_result}")
    else:
        st.write(f"No results found for {table_name.capitalize()}.")


def display_query_result2(result, selected_columns, table_name):
    if result:
        st.write(f"Query Result for {table_name.capitalize()}:")
        # Display relevant columns and their values
        for row in result:
            st.write(", ".join(f"{col}: {value}" for col, value in zip(selected_columns, row)))
    else:
        st.write(f"No results found for {table_name.capitalize()}.")

def main():
    st.title(":blue[Mall management system] :mall")
    x = st.sidebar.radio("Choose", ["Customers", "Employees", "Products"])
    menu = ["Add", "View", "Edit", "Remove"]
    choice = st.sidebar.selectbox("Menu", menu)
    st.sidebar.markdown("<br>" * 8, unsafe_allow_html=True)
    #st.sidebar.button("Simple Queries")
    #st.sidebar.button("Nested Queries")
    #st.sidebar.button("Correlated Queries")
    if st.sidebar.button("Total product"):
        total_product_frontend()

    if x == "Customers":
        create_customer_table()
        colorc = '#ffd166'
        if choice == "Add":
            st.markdown(f'<h3 style="color:{colorc}">Enter Customer details</h3>', unsafe_allow_html=True)
            create_customer()

        elif choice == "View":
            st.markdown(f'<h3 style="color:{colorc}">View Customer details</h3>', unsafe_allow_html=True)
            read_customers()

        elif choice == "Edit":
            st.markdown(f'<h3 style="color:{colorc}">Edit Customer details</h3>', unsafe_allow_html=True)
            update_customer()

        elif choice == "Remove":
            st.markdown(f'<h3 style="color:{colorc}">Delete Customer details</h3>', unsafe_allow_html=True)
            delete_customers()

        else:
            st.subheader("CRUD Options for Customers")

    elif x == "Employees":
        create_employee_table()
        colore = '#06d6a0'
        if choice == "Add":
            st.markdown(f'<h3 style="color:{colore}">Enter Employee details</h3>', unsafe_allow_html=True)
            create_employee()

        elif choice == "View":
            st.markdown(f'<h3 style="color:{colore}">View Employee details</h3>', unsafe_allow_html=True)
            read_employees()

        elif choice == "Edit":
            st.markdown(f'<h3 style="color:{colore}">Edit Employee details</h3>', unsafe_allow_html=True)
            update_employee()

        elif choice == "Remove":
            st.markdown(f'<h3 style="color:{colore}">Delete Employee details</h3>', unsafe_allow_html=True)
            delete_employees()

        else:
            st.subheader("CRUD Options for Employees")

    elif x == "Products":
        create_product_table()
        colorp = "#ef233c"
        if choice == "Add":
            st.markdown(f'<h3 style="color:{colorp}">Enter product details</h3>', unsafe_allow_html=True)
            create_product()

        elif choice == "View":
            st.markdown(f'<h3 style="color:{colorp}">View product details</h3>', unsafe_allow_html=True)
            read_products()

        elif choice == "Edit":
            st.markdown(f'<h3 style="color:{colorp}">Edit product details</h3>', unsafe_allow_html=True)
            update_product()

        elif choice == "Remove":
            st.markdown(f'<h3 style="color:{colorp}">Delete any product</h3>', unsafe_allow_html=True)
            delete_products()

        else:
            st.subheader("CRUD Options for Products")


if __name__ == '__main__':
    main()


# Streamlit UI
st.title("Query Executor")

# Dropdown to select the table for simple query
selected_table_simple = st.selectbox("Select Table for Simple Query:", ["customer", "employee", "product"])

if st.button("Execute Simple Query"):
    result_simple, column_names_simple = execute_default_query(selected_table_simple)
    display_query_result(result_simple, column_names_simple, selected_table_simple)

# Dropdown for choosing between "Employee" and "Product" for nested query
selected_table_nested = st.selectbox("Select Table for Nested Query:", ["employee", "product"])

# Execute Nested Query
if st.button("Execute Nested Query"):
    result_nested = execute_nested_query(selected_table_nested)
    display_query_result1(result_nested, ["Count"], selected_table_nested)

# Dropdown for choosing Employee for correlated query
selected_table_correlated = st.selectbox("Select Table for Correlated Query:", ["employee"])

# Execute Correlated Query
if st.button("Execute Correlated Query"):
    result_correlated = execute_correlated_query(selected_table_correlated)
    # Specify the columns you want to display in the result
    display_query_result2(result_correlated, ["employee_id", "name", "contact_info", "salary"], selected_table_correlated)

