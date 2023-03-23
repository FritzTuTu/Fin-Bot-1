import certifi
import json
import math
import requests

apikey = "6773f916da46be1f54613e01994d476d"

def get_jsonparsed_data(url):
    """
    Receive the content of ``url``, parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = requests.get(url, verify=certifi.where())
    return response.json()

def intrinsic_value():
    # Prompt the user to enter the required information
    stock_code = input("Enter the stock ticker symbol: ")
    growth_rate = float(input("Enter the expected growth rate as a decimal: "))
    discount_rate = float(input("Enter the discount rate as a decimal: "))
    depreciation = float(input("Enter the depreciation and amortization for the company: "))
    cash_and_cash_equivalents = float(input("Enter the cash and cash equivalents for the company: "))

    # Get the net income, capital expenditure, and debt data from the API
    url = f"https://financialmodelingprep.com/api/v3/financials/income-statement/{stock_code}?apikey={apikey}"
    data = get_jsonparsed_data(url)
    net_income = float(data['financials'][0]['Net Income'])
    url = f"https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/{stock_code}?apikey={apikey}"
    data = get_jsonparsed_data(url)
    capital_expenditure = float(data['financials'][0]['Capital Expenditure'])
    total_debt = float(data['financials'][0]['Total debt'])

    # Calculate the present value of the residual value
    residual_value = (net_income + depreciation - capital_expenditure) * (1 + growth_rate) / (discount_rate - growth_rate)
    # Calculate the sum of present discounts
    present_discounts = 0
    for i in range(1, 6):
        present_discounts += (net_income + depreciation - capital_expenditure) / math.pow((1 + discount_rate), i)
    # Calculate the intrinsic value
    intrinsic_value = present_discounts + (cash_and_cash_equivalents - total_debt) + residual_value

    return intrinsic_value

# Example usage
intrinsic_val = intrinsic_value()
print(f"The intrinsic value of the company is ${intrinsic_val:.2f}")


