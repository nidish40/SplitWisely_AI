# SplitWiselyAI Analyzer - Bank Statement Analysis

Welcome to the **SplitWiselyAI Analyzer**! This app helps you analyze your bank statements by categorizing your spending, comparing it to predefined budget categories, and providing insightful analysis to help you manage your finances better.

## Features

- **Categorizes Transactions**: Automatically categorizes your transactions based on descriptions using Gemini AI.
- **Budget Management**: Set custom budget limits for predefined categories (e.g., Groceries, Rent, Utilities).
- **Data Visualization**: Displays your spending by category with interactive pie charts.
- **Insights Generation**: Ask questions about your spending, and get personalized insights from the SplitWiselyAI model.
- **Budget Analysis**: Compares your spending with the budget limits and provides an analysis of your financial health.

## Requirements

To run this app locally, you need:

- Python 3.7 or higher
- Streamlit
- Pandas
- Altair
- Gemini API for transaction categorization
- A valid bank statement in CSV format (with columns: Date, Description, Amount)

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/splitwiselyai-analyzer.git
    ```

2. Navigate to the project folder:
    ```bash
    cd splitwiselyai-analyzer
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Gemini API (if required by the app):
    - Ensure you have a valid Gemini API key and configure it accordingly in the code.

## Usage

1. **Run the App**:
    - Start the app by running the following command:
      ```bash
      streamlit run app.py
      ```

2. **Upload Bank Statement**:
    - Upload your bank statement in CSV format. The CSV file must contain at least the following columns:
        - `Date`: The date of the transaction.
        - `Description`: The description or label for the transaction.
        - `Amount`: The monetary amount of the transaction.

3. **Set Budget Limits**:
    - Set budget limits for the predefined categories (Groceries, Rent, Utilities, etc.) using the slider inputs.

4. **View Analysis**:
    - After uploading your CSV, the app will categorize your transactions and show the categorized data.
    - It will then display a pie chart representing your spending across different categories.
    - The app will also show a budget analysis, comparing your actual spending to your set budget limits.
    - You can ask questions about your spending, and the app will provide insights based on Gemini's response.

## Features Breakdown

### 1. **Transaction Categorization**:
- The app uses the Gemini API to categorize your transactions based on their descriptions.
- After categorization, the transactions are grouped into predefined categories like `Groceries`, `Rent`, `Utilities`, and more.

### 2. **Budget Limits**:
- You can define a budget for each predefined category using the slider inputs.
- Categories available for budget setting:
  - Groceries
  - Rent
  - Utilities
  - Entertainment
  - Other

### 3. **Data Visualization**:
- The app generates a **pie chart** that displays your spending across the different categories. This chart allows you to quickly understand where most of your money is being spent.

### 4. **Budget Analysis**:
- After the categorization, the app compares your actual spending with your budget limits.
- It provides a summary of whether you are staying within your budget or exceeding it, helping you make informed decisions about your finances.

### 5. **Insights Generation**:
- Users can ask specific questions about their spending.
- Example questions could include:
  - "How much did I spend on groceries this month?"
  - "What are the top categories where I exceeded my budget?"
- The app uses the Gemini API to generate personalized insights based on your spending data.

## Troubleshooting

### 1. **CSV Format Issues**:
- Ensure that the CSV file contains the required columns: `Date`, `Description`, and `Amount`. If any of these are missing, the app will display an error.
- Make sure the CSV is properly formatted with no extra commas or empty rows.

### 2. **Gemini API Errors**:
- If there's an issue with the Gemini API, ensure that you have the correct API key and that the API is accessible.
- Check your internet connection and API limits if categorization fails.

### 3. **App Performance**:
- If the app is slow or unresponsive, try uploading a smaller CSV file or check if the dataset has too many rows.
- You can also try caching the results for faster performance.

## Example Questions for Insights

- "How much did I spend on groceries last month?"
- "What category am I spending the most on?"
- "Did I exceed my budget for entertainment?"
- "Can you summarize my spending trends for this month?"

## Future Improvements

- **Multi-file support**: Support for uploading multiple CSV files for analysis.
- **More category options**: Allow users to add their own categories for transactions.
- **Detailed spending trends**: Provide line charts or bar charts showing spending over time.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the creators of Gemini API for providing the categorization functionality.
- This project uses Streamlit for the interactive app interface.
- Altair is used for visualizing spending data through charts.



