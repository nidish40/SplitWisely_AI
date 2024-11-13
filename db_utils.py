import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to connect to MySQL database using credentials from .env
def connect_to_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),  # Get DB host from .env
        user=os.getenv("DB_USER"),  # Get DB user from .env
        password=os.getenv("DB_PASSWORD"),  # Get DB password from .env
        database=os.getenv("DB_NAME")  # Get DB name from .env
    )

# Function to insert only price and category into the transactions table
def insert_transactions(transactions_df):
    conn = connect_to_db()
    cursor = conn.cursor()

    # SQL Insert query (only price and category)
    for _, row in transactions_df.iterrows():
        cursor.execute("""
            INSERT INTO transactions (price, category)
            VALUES (%s, %s)
        """, (row['price'], row['category']))

    conn.commit()
    cursor.close()
    conn.close()

# Function to retrieve transactions from the database
def get_transactions():
    conn = connect_to_db()
    cursor = conn.cursor()

    # SQL query to get all transactions (price, category)
    cursor.execute("SELECT price, category FROM transactions")
    transactions = cursor.fetchall()

    # Convert the result into a DataFrame
    transactions_df = pd.DataFrame(transactions, columns=["price", "category"])

    cursor.close()
    conn.close()

    return transactions_df
