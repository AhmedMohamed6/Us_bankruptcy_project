# Import necessary libraries.
import streamlit as st
import pandas as pd
import joblib

# Load the trained model and feature names
model = joblib.load("model.pkl")
inputs = joblib.load("inputs.pkl")

# Define a function for making predictions
def prediction(Current_Assets, Cost_of_Goods_Sold, Depreciation_and_Amortization,
       EBITDA, Inventory, Net_Income, Total_Receivables,
       Market_Value, Net_Sales, Total_Assets, Total_Long_term_Debt,
       Total_Current_Liabilities, Retained_Earnings, Total_Liabilities,
       Total_Operating_Expenses):
    # Create a DataFrame with columns based on feature names.
    df = pd.DataFrame(columns=inputs)
    # Set the provided input values in the DataFrame.
    df.at[0, 'Current_Assets'] = Current_Assets
    df.at[0, 'Cost_of_Goods_Sold'] = Cost_of_Goods_Sold
    df.at[0, 'Depreciation_and_Amortization'] = Depreciation_and_Amortization
    df.at[0, 'EBITDA'] = EBITDA
    df.at[0, 'Inventory'] = Inventory
    df.at[0, 'Net_Income'] = Net_Income
    df.at[0, 'Total_Receivables'] = Total_Receivables
    df.at[0, 'Market_Value'] = Market_Value
    df.at[0, 'Net_Sales'] = Net_Sales
    df.at[0, 'Total_Assets'] = Total_Assets
    df.at[0, 'Total_Long_term_Debt'] = Total_Long_term_Debt
    df.at[0, 'Total_Current_Liabilities'] = Total_Current_Liabilities
    df.at[0, 'Retained_Earnings'] = Retained_Earnings
    df.at[0, 'Total_Liabilities'] = Total_Liabilities
    df.at[0, 'Total_Operating_Expenses'] = Total_Operating_Expenses
    # Use the model to make predictions.
    res = model.predict(df)
    return res[0]

# Define the main function for the Streamlit app.
def main():
    # Create a Streamlit web interface.
    st.title("Bankruptcy Prediction")
    
    # Create input fields for user input
    features = [
        "Current Assets", "Cost of Goods Sold", "Depreciation and Amortization",
        "EBITDA", "Inventory", "Net Income", "Total Receivables",
        "Market Value", "Net Sales", "Total Assets", "Total Long-term Debt",
        "Total Current Liabilities", "Retained Earnings", "Total Liabilities",
        "Total Operating Expenses"
    ]

    input_values = [st.text_input(feature) for feature in features]

    if st.button("Predict"):
        # Call the prediction function and display the result
        result = prediction(*input_values)
        st.write(f"Prediction for this company is: {'Not Bankrupt' if result == 1 else 'Bankrupt'}")

main()
