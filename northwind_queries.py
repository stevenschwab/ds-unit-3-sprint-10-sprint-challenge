'''Queries for northwind db'''

"""What are the ten most expensive items (per unit price) 
in the database? Please return all columns in the table, 
not just the price and name but all columns."""
EXPENSIVE_ITEMS = '''
    SELECT * 
    FROM Products
    ORDER BY Price DESC
    LIMIT 10;
'''

QUERY_LIST = [
    EXPENSIVE_ITEMS
]