
'''
import pandas as pd
import streamlit as st
from database1 import view_all_customers

def read_customers():
    result = view_all_customers()
    df = pd.DataFrame(result, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])
    
    with st.expander("View all Customers"):
        st.dataframe(df)

from database1 import view_all_employees

def read_employees():
    result = view_all_employees()
    df = pd.DataFrame(result, columns=['Employee ID', 'Name', 'Salary', 'Contact Info','Employee Type','Department'])
    
    with st.expander("View all Employees"):
        st.dataframe(df)


from database1 import view_all_products

def read_products():
    result = view_all_products()
    df = pd.DataFrame(result, columns=['Product ID', 'Quantity', 'Name', 'Type', 'Price'])

    with st.expander("View all Products"):
        st.dataframe(df)
'''



import pandas as pd
import streamlit as st
from database1 import view_all_customers

def read_customers():
    result = view_all_customers()
    df = pd.DataFrame(result, columns=['Customer ID', 'First Name', 'Last Name', 'Email', 'Phone Number'])
    
    with st.expander("View all Customers"):
        st.dataframe(df)

from database1 import view_all_employees

def read_employees():
    result = view_all_employees()
    df = pd.DataFrame(result, columns=['Employee ID', 'Name', 'Salary', 'Contact Info','employee_type','Department'])
    
    with st.expander("View all Employees"):
        st.dataframe(df)


from database1 import view_all_products

def read_products():
    result = view_all_products()
    df = pd.DataFrame(result, columns=['Product ID', 'Quantity', 'Name', 'Type', 'Price','Total_Val'])

    with st.expander("View all Products"):
        st.dataframe(df)
