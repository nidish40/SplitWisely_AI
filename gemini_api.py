import google.generativeai as genai
from google.generativeai.types import RequestOptions
from google.api_core import retry
import pandas as pd
from dotenv import load_dotenv
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

def categorize_transactions_with_gemini(df):
    categories = []
    for description in df["Description"]:
        prompt = f"Categorize the following transaction: {description}. Categories: Groceries, Rent, Utilities, Entertainment, or Other. Only return one word."
        response = model.generate_content(
            prompt,
            request_options=RequestOptions(
                retry=retry.Retry(initial=1, multiplier=1, maximum=60, timeout=10)
            )
        )
        category = response.text.strip()
        categories.append(category)
    df["Category"] = categories
    return df

def generate_spending_report(df):
    report = df.groupby("Category")["Amount"].sum().reset_index()
    return report

def answer_gemini(question, df):
    prompt = f"Based on the following categorized transactions, answer the question: {question}\n\n"
    for index, row in df.iterrows():
        prompt += f"Transaction: {row['Description']}, Category: {row['Category']}, Amount: {row['Amount']}\n"
    response = model.generate_content(
        prompt,
        request_options=RequestOptions(
            retry=retry.Retry(initial=1, multiplier=1, maximum=60, timeout=10)
        )
    )
    return response.text

def analyze_budget(df, budget_limits=None):
    if budget_limits is None:
        budget_limits = {} 

    report = generate_spending_report(df)
    report["Budget_Limit"] = report["Category"].map(budget_limits)
    report["Surplus/Deficit"] = report["Budget_Limit"] + report["Amount"]

    analysis_summary = ""


    for _, row in report.iterrows():
        category = row["Category"]
        surplus_deficit = row["Surplus/Deficit"]
        if surplus_deficit >= 0:
            analysis_summary += f"{category}: Within budget. Surplus of {surplus_deficit}.\n"
        else:
            analysis_summary += f"{category}: Exceeded budget by {-surplus_deficit}.\n"

    return report, analysis_summary