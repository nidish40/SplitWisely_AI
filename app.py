""" import streamlit as st
import pandas as pd
from gemini_api import get_gemini_response
import io

# Initialize the list of transactions in Streamlit session state
if "transactions" not in st.session_state:
    st.session_state.transactions = []

# Display the title of the app
st.title("Budget Recommender")

# Option for file upload (CSV)
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# Option for manually entering transactions
st.subheader("Enter transactions manually")

# Input fields for manual transaction entry
description = st.text_input("Transaction Description")
price = st.number_input("Transaction Price", min_value=0.0, format="%.2f")
category = st.text_input("Transaction Category")

# Add button to manually add the transaction
if st.button("Add Transaction"):
    if description and price and category:
        # Append the transaction to the session state list
        st.session_state.transactions.append({"description": description, "price": price, "category": category})
        st.success("Transaction added successfully!")
    else:
        st.error("Please fill all fields")

# Button to process transactions (either from CSV or manually entered)
if st.button("Budget Recommendation & Analysis"):
    # Check if transactions are loaded
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        # Assuming CSV has 'description', 'price', 'category' columns
        transactions_df = df[['description', 'price', 'category']]
        st.write("Transactions from CSV:", transactions_df)  # Show the DataFrame from CSV
    elif st.session_state.transactions:
        # Convert the list of transactions in session state to a DataFrame
        transactions_df = pd.DataFrame(st.session_state.transactions)
        st.write("Transactions manually entered:", transactions_df)  # Show the DataFrame from manual input
    else:
        st.error("Please upload a CSV file or enter transactions manually.")
        transactions_df = None

    # If transactions were successfully gathered, send them to Gemini for processing
    if transactions_df is not None and not transactions_df.empty:
        

        # Send the DataFrame to Gemini and get the recommendation
        try:
            recommendation = get_gemini_response(transactions_df)
            st.write("Budget Recommendation from Gemini:")
            st.write(recommendation)
        except Exception as e:
            st.error(f"Error while getting response from Gemini: {e}")
    else:
        st.error("No transactions to send or empty DataFrame.")
 """

import streamlit as st
import pandas as pd
from gemini_api import get_gemini_response
import io

# Initialize the list of transactions in Streamlit session state
if "transactions" not in st.session_state:
    st.session_state.transactions = []

# Custom CSS for a dark theme with improved styling
st.markdown("""
    <style>
    .stApp {
        background-color: #1E1E1E;
        color: #E0E0E0;
    }
    .main-header {
        color: #FFA500;
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .subheader {
        color: #FFA500;
        font-size: 1.5em;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .stTextInput, .stNumberInput {
        background-color: #333 !important;
        color: #E0E0E0 !important;
        border: 1px solid #444 !important;
    }
    .stButton>button {
        background-color: #4CAF50 !important;
        color: white !important;
        font-weight: bold;
        padding: 8px 16px !important;
        border-radius: 5px !important;
    }
    .stButton>button:hover {
        background-color: #45A049 !important;
    }
    .error-message {
        color: #DC3545;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the title of the app with custom styling
st.markdown("<div class='main-header'>Budget Recommender</div>", unsafe_allow_html=True)

# Option for file upload (CSV)
uploaded_file = st.file_uploader("Upload a CSV file", type="csv", help="Upload a CSV file with columns 'description', 'price', and 'category'.")

# Option for manually entering transactions
st.markdown("<div class='subheader'>Enter transactions manually</div>", unsafe_allow_html=True)

# Input fields for manual transaction entry with dark theme styling
description = st.text_input("Transaction Description", key="description", placeholder="Enter transaction description")
price = st.number_input("Transaction Price", min_value=0.0, format="%.2f", key="price")
category = st.text_input("Transaction Category", key="category", placeholder="Enter transaction category")

# Add button to manually add the transaction
if st.button("Add Transaction", key="add_button", help="Add your transaction to the list"):
    if description and price and category:
        # Append the transaction to the session state list
        st.session_state.transactions.append({"description": description, "price": price, "category": category})
        st.success("Transaction added successfully!", icon="✅")
    else:
        st.error("Please fill all fields", icon="⚠️")

# Button to process transactions (either from CSV or manually entered)
if st.button("Budget Recommendation & Analysis", key="process_button"):
    # Check if transactions are loaded
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        # Assuming CSV has
        # 'description', 'price', 'category' columns
        transactions_df = df[['description', 'price', 'category']]
        st.write("Transactions from CSV:", transactions_df)  # Show the DataFrame from CSV
    elif st.session_state.transactions:
        # Convert the list of transactions in session state to a DataFrame
        transactions_df = pd.DataFrame(st.session_state.transactions)
        st.write("Transactions manually entered:", transactions_df)  # Show the DataFrame from manual input
    else:
        st.error("Please upload a CSV file or enter transactions manually.", icon="⚠️")
        transactions_df = None

    # If transactions were successfully gathered, send them to Gemini for processing
    if transactions_df is not None and not transactions_df.empty:
        with st.spinner("Fetching budget recommendation from Gemini..."):
            try:
                # Send the DataFrame to Gemini and get the recommendation
                recommendation = get_gemini_response(transactions_df)
                st.markdown("<div class='subheader'>Budget Recommendation:</div>", unsafe_allow_html=True)
                st.write(recommendation)
            except Exception as e:
                st.error(f"Error while getting response from Gemini: {e}", icon="⚠️")
    else:
        st.error("No transactions to send or empty DataFrame.", icon="⚠️")
