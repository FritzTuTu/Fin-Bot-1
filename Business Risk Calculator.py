
import requests
import numpy

api_key = "6773f916da46be1f54613e01994d476d"
stocks = ['AAPL','MSFT','GOOG']
for stock in stocks:
    #The code extracts each company's metrics and appends the extracted values into a list. Each of the list will contain the latest 5 year company operation.
    income_statement = requests.get(f'https://financialmodelingprep.com/api/v3/income-statement/{stock}?apikey={api_key}').json()

    number_of_years = 0
    revenues = []
    operating_income = []
    net_income = []

    for item in income_statement:
        if number_of_years < 5:
            revenues.append(income_statement[number_of_years]['revenue'])
            operating_income.append(income_statement[number_of_years]['operatingIncome'])
            net_income.append(income_statement[number_of_years]['netIncome'])
            number_of_years +=1

    print(revenues)

    #The code then converts them into arrays using numpy
    revenues_array = numpy.array(revenues)
    operating_income_array = numpy.array(operating_income)
    net_income_array = numpy.array(net_income)

    #We apply our coefficient of variation formula to each of the metrics
    CV_Sales = revenues_array.std() /revenues_array.mean()

    print('Revenue Coefficient of Variation for ' + stock + ' is ' + str(round(CV_Sales,2)))
    CV_OI = operating_income_array.std() /operating_income_array.mean()

    print('Operating Income Coefficient of Variation for ' + stock + ' is ' + str(round(CV_OI,2)))
    CV_Net_Income = net_income_array.std() /net_income_array.mean()

    print('Net Income Coefficient of Variation for ' + stock + ' is ' + str(round(CV_Net_Income,2)) + '\n')
