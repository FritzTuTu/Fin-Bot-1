import pandas as pd
import numpy as np
from scipy.optimize import minimize

# define the securities in the portfolio and their weights
tickers = ['AAPL', 'MSFT', 'GOOG', 'TSLA']
weights = np.array([0.3, 0.2, 0.2, 0.3])

# define the time period for the analysis
start_date = '2018-01-01'
end_date = '2021-12-31'

# download historical data from Yahoo Finance
data = pd.DataFrame()
for ticker in tickers:
    temp_data = pd.read_csv(f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1=1514764800&period2=1640947200&interval=1mo&events=history&includeAdjustedClose=true')
    temp_data.set_index('Date', inplace=True)
    data[ticker] = temp_data['Adj Close']

# calculate the monthly returns of the securities
returns = data.pct_change().dropna()

# calculate the expected returns and covariance matrix of the securities
mu = returns.mean()
Sigma = returns.cov()

# define the objective function to minimize
def portfolio_volatility(weights, Sigma):
    return np.sqrt(np.dot(weights.T, np.dot(Sigma, weights)))

# define the constraints for the optimization
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

# define the bounds for the optimization
bounds = tuple((0, 1) for i in range(len(tickers)))

# perform the optimization to find the optimal weights
result = minimize(portfolio_volatility, weights, args=(Sigma,), method='SLSQP', bounds=bounds, constraints=constraints)
optimal_weights = result.x

# calculate the returns and volatility of the optimal portfolio
portfolio_returns = (returns * optimal_weights).sum(axis=1)
portfolio_volatility = portfolio_volatility(optimal_weights, Sigma)

# print the results
print(f"Optimal Portfolio Weights: {optimal_weights}")
print(f"Optimal Portfolio Annualized Return: {np.sum(mu * optimal_weights) * 12:.2%}")
print(f"Optimal Portfolio Annualized Volatility: {portfolio_volatility * np.sqrt(12):.2%}")

