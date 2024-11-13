import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API key for Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro")

# Function to interact with Gemini API and get recommendations
def get_gemini_response(transactions_df):
    try:
        transaction_text = ""
    
        # Convert the transaction DataFrame to a prompt for Gemini
        for index, row in transactions_df.iterrows():
            description = row['description']
            price = row['price']
            category = row['category']
            
            # Build a simple summary or prompt for Gemini based on transaction details
            transaction_text += f"Transaction: {description}, Price: {price}, Category: {category}\n"
        
        # Final prompt for Gemini
        prompt = f"All the transactions are in rupees. Here are some transactions:\n{transaction_text}\nCan you provide a budget recommendation for these?"
        
        # Get the response from Gemini
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        print(f"Error generating Gemini response: {e}")
        raise Exception(f"Error generating Gemini response: {e}")
