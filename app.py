import os
import pandas as pd
import streamlit as st
import altair as alt
from gemini_api import categorize_transactions_with_gemini, answer_gemini, analyze_budget

# Configure Streamlit
st.set_page_config(page_title="SplitWiselyAI Analyzer", page_icon="💳")

st.title("Bank Statement Analyzer")
st.markdown("""
    Upload your bank statement in CSV format to analyze spending and categorize your transactions.
    You can set budget limits for predefined categories such as Groceries, Rent, Utilities, and others.
""")

# Predefined budget categories
PREDEFINED_CATEGORIES = ['Groceries', 'Rent', 'Utilities', 'Entertainment', 'Other']

# User input for custom budget categories and limits
st.markdown("### Set Budget Limits for Predefined Categories")
budget_categories = {}
for category in PREDEFINED_CATEGORIES:
    limit = st.number_input(f"Set budget limit for {category}", min_value=0.0, key=category)
    budget_categories[category] = limit

# File uploader for CSV file
uploaded_file = st.file_uploader("Upload CSV Bank Statement", type=["csv"])

if uploaded_file is not None:
    try:
        # Load CSV file into DataFrame
        df = pd.read_csv(uploaded_file)

        # Ensure necessary columns exist in the DataFrame
        if {'Date', 'Description', 'Amount'}.issubset(df.columns):
            # Categorize transactions using Gemini
            with st.spinner("Organizing your spendings..."):
                df = categorize_transactions_with_gemini(df)

            # Display categorized transactions
            st.subheader("Transactions with Categories")
            st.write(df)

            # Display spending by category as a pie chart
            st.subheader("Spending by Category (Pie Chart)")
            category_totals = df.groupby("Category")["Amount"].sum().reset_index()
            
            pie_chart = alt.Chart(category_totals).mark_arc().encode(
                theta=alt.Theta(field="Amount", type="quantitative"),
                color=alt.Color(field="Category", type="nominal"),
                tooltip=["Category", "Amount"]
            ).properties(
                width=400,
                height=400
            )

            st.altair_chart(pie_chart)

            # Perform budget analysis and display results
            budget_report, analysis_summary = analyze_budget(df, budget_limits=budget_categories)
            st.subheader("SplitWiselyAI Analysis")
            st.write(budget_report)
            st.text(analysis_summary)

            # Allow the user to ask specific questions about spending
            question = st.text_input("Ask a question about your spending to SplitWiselyAI:")

            if question:
                with st.spinner("Generating insights..."):
                    response = answer_gemini(question, df)
                st.subheader("SplitWiselyAI Response")
                st.write(response)
        else:
            st.error("CSV file must contain 'Date', 'Description', and 'Amount' columns.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.warning("Please upload a CSV file to proceed.")